#!/usr/bin/env python3
"""equilibrio.py — empurra o G1 parado e acompanha o centro de massa (CoM) contra o polígono de apoio.

Uso: python3 kit/equilibrio.py --empurrao NEWTONS [--duracao 0.2]
O empurrão é uma força horizontal (para a frente, +x) no tronco, aplicada em t = 0,5 s.
O G1 só segura a pose "stand" com os atuadores de posição do modelo: não há controlador de equilíbrio.
Polígono de apoio = envoltória convexa dos pontos de contato dos pés com o chão (força > 1 N).
Margem = distância da projeção do CoM até a borda do polígono (positiva = dentro).
CoP = centro de pressão (média dos pontos de contato pesada pela força normal); no chão plano é o ZMP.
"""
import argparse
import sys

import mujoco
import numpy as np

import fth


def envoltoria(pts):
    pts = sorted(set(pts))
    if len(pts) <= 2:
        return pts
    def giro(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    baixo, cima = [], []
    for p in pts:
        while len(baixo) >= 2 and giro(baixo[-2], baixo[-1], p) <= 0:
            baixo.pop()
        baixo.append(p)
    for p in reversed(pts):
        while len(cima) >= 2 and giro(cima[-2], cima[-1], p) <= 0:
            cima.pop()
        cima.append(p)
    return baixo[:-1] + cima[:-1]  # sentido anti-horário


def dist_segmento(p, a, b):
    p, a, b = map(np.asarray, (p, a, b))
    ab = b - a
    t = 0.0 if not ab.any() else float(np.clip(np.dot(p - a, ab) / np.dot(ab, ab), 0, 1))
    return float(np.linalg.norm(p - (a + t * ab)))


def margem(p, poli):
    if not poli:
        return -1.0
    if len(poli) < 3:
        return -dist_segmento(p, poli[0], poli[-1])
    dentro = True
    for i in range(len(poli)):
        a, b = poli[i], poli[(i + 1) % len(poli)]
        if (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0]) < 0:
            dentro = False
    d = min(dist_segmento(p, poli[i], poli[(i + 1) % len(poli)]) for i in range(len(poli)))
    return d if dentro else -d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--empurrao", type=float, required=True, help="força em newtons")
    ap.add_argument("--duracao", type=float, default=0.2, help="duração do empurrão em segundos")
    a = ap.parse_args()
    m = fth.carregar("unitree_g1/scene.xml")
    d = mujoco.MjData(m)
    fth.pose_inicial(m, d)
    tronco = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, "torso_link")
    pelve = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_BODY, "pelvis")
    print(f"empurrão de {a.empurrao:.0f} N por {a.duracao:.1f} s no tronco (t = 0.5 s) · impulso {a.empurrao * a.duracao:.0f} N·s")
    print(f"{'t (s)':>5} {'margem do CoM (cm)':>19} {'CoP x (cm)':>11} {'pelve z (m)':>12}")
    saiu = None
    passos = int(3.0 / m.opt.timestep)
    for i in range(passos + 1):
        t = d.time
        d.xfrc_applied[tronco, :3] = [a.empurrao, 0, 0] if 0.5 <= t < 0.5 + a.duracao else [0, 0, 0]
        mujoco.mj_forward(m, d)
        _, pontos = fth.forca_pes(m, d)
        pts = [(x, y, f) for lista in pontos.values() for (x, y, f) in lista if f > 1.0]
        poli = envoltoria([(round(x, 4), round(y, 4)) for x, y, _ in pts])
        com = d.subtree_com[pelve][:2]
        mg = margem(tuple(com), poli)
        ftot = sum(f for _, _, f in pts)
        cop = sum(x * f for x, _, f in pts) / ftot if ftot else float("nan")
        if saiu is None and mg < 0:
            saiu = t
        if i % 125 == 0:
            print(f"{t:>5.2f} {100 * mg:>19.1f} {100 * cop:>11.1f} {d.qpos[2]:>12.2f}")
        if i < passos:
            mujoco.mj_step(m, d)
    caiu = d.qpos[2] < 0.5
    if saiu is None:
        print("CoM dentro do apoio: sim (o tempo todo)")
    else:
        print(f"CoM dentro do apoio: não · saiu em t = {saiu:.2f} s")
    print(f"queda: {'sim' if caiu else 'não'} (pelve a {d.qpos[2]:.2f} m em t = 3 s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
