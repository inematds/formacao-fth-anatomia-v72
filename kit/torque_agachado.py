#!/usr/bin/env python3
"""torque_agachado.py — quanto torque cada junta faz para o G1 ficar agachado parado.

Uso: python3 kit/torque_agachado.py [--joelho GRAUS] [--modelo unitree_g1/scene.xml]
Parte da pose "stand", dobra o joelho em GRAUS (quadril e tornozelo dobram a metade, pé fica plano),
segura 2 s com os atuadores de posição do modelo e lê o torque de cada junta (d.qfrc_actuator).
Depois confere o joelho por dinâmica inversa (mj_inverse) na mesma pose: os dois caminhos têm de bater.
"""
import argparse
import math
import sys

import mujoco
import numpy as np

import fth

PERNA = ("hip_pitch_joint", "knee_joint", "ankle_pitch_joint")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--joelho", type=float, default=90.0, help="dobra do joelho em graus (0 = em pé)")
    ap.add_argument("--modelo", default="unitree_g1/scene.xml")
    a = ap.parse_args()
    m = fth.carregar(a.modelo)
    d = mujoco.MjData(m)
    fth.pose_inicial(m, d)
    ids = {fth.nome(m, mujoco.mjtObj.mjOBJ_ACTUATOR, i): i for i in range(m.nu)}
    k = math.radians(a.joelho)
    alvo = d.ctrl.copy()
    for lado in ("left", "right"):
        for nomej, ang in zip(PERNA, (-k / 2, k, -k / 2)):
            alvo[ids[f"{lado}_{nomej}"]] = ang
    c0 = d.ctrl.copy()
    n = int(2.0 / m.opt.timestep)
    for i in range(n):
        f = min(1.0, i / (0.5 * n))  # 1 s de rampa, 1 s parado
        d.ctrl[:] = c0 + (alvo - c0) * f
        mujoco.mj_step(m, d)
    art = fth.juntas_articuladas(m)
    tq = {j: abs(d.qfrc_actuator[m.jnt_dofadr[j]]) for j in art}
    ordem = sorted(art, key=lambda j: (-round(tq[j]), fth.nome(m, mujoco.mjtObj.mjOBJ_JOINT, j)))  # empate: ordem alfabética
    print(f"joelho dobrado {a.joelho:.0f}° · altura da pelve {d.qpos[2]:.2f} m · {d.ncon} contatos com o chão")
    if d.qpos[2] < 0.4:
        print("ATENÇÃO: o robô caiu.")
        print("O centro de massa saiu de cima dos pés; os torques abaixo não são de agachamento (aula 6).")
    print(f"{'junta':<28} {'torque (N·m)':>13} {'limite':>7} {'% do limite':>12}")
    for j in ordem[:4]:
        lim = fth.limite_torque(m, j)
        print(f"{fth.nome(m, mujoco.mjtObj.mjOBJ_JOINT, j):<28} {tq[j]:>13.0f} {lim:>7.0f} {100 * tq[j] / lim:>11.0f}%")
    # conferência por dinâmica inversa: mesma pose, velocidade e aceleração zero
    d2 = mujoco.MjData(m)
    d2.qpos[:] = d.qpos
    mujoco.mj_inverse(m, d2)
    j0 = ordem[0]
    inv = abs(d2.qfrc_inverse[m.jnt_dofadr[j0]])
    print(f"conferência mj_inverse ({fth.nome(m, mujoco.mjtObj.mjOBJ_JOINT, j0)}): {inv:.0f} N·m")
    jl = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, "left_knee_joint")
    jr = mujoco.mj_name2id(m, mujoco.mjtObj.mjOBJ_JOINT, "right_knee_joint")
    if jl >= 0 and jr >= 0:
        print(f"joelhos: esquerdo {tq[jl]:.0f} N·m · direito {tq[jr]:.0f} N·m")
    print(f"maior torque: {fth.nome(m, mujoco.mjtObj.mjOBJ_JOINT, j0)} {tq[j0]:.0f} N·m")
    return 0


if __name__ == "__main__":
    sys.exit(main())
