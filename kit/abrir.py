#!/usr/bin/env python3
"""abrir.py — abre um humanoide do MuJoCo Menagerie e mostra o tamanho do modelo.

Uso: python3 kit/abrir.py unitree_g1/scene.xml
nq = coordenadas de posição (a base flutuante usa 7: x, y, z + quatérnio de 4)
nv = velocidades (a base usa 6: 3 lineares + 3 angulares)
nu = atuadores (motores que você comanda)
"""
import sys

import mujoco

import fth


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 2
    m = fth.carregar(sys.argv[1])
    d = mujoco.MjData(m)
    fth.pose_inicial(m, d)
    livres = sum(1 for j in range(m.njnt) if m.jnt_type[j] == mujoco.mjtJoint.mjJNT_FREE)
    print(f"modelo: {m.names.split(b'\0')[0].decode()} · arquivo {sys.argv[1]}")
    print(f"nq={m.nq} nv={m.nv} nu={m.nu}")
    print(f"juntas: {m.njnt} ({livres} base flutuante + {m.njnt - livres} articuladas) · corpos: {m.nbody - 1} · sensores: {m.nsensor}")
    print(f"massa total do modelo: {sum(m.body_mass):.1f} kg · passo de simulação: {m.opt.timestep * 1000:.0f} ms")
    keys = [fth.nome(m, mujoco.mjtObj.mjOBJ_KEY, k) for k in range(m.nkey)]
    print(f"poses salvas (keyframes): {', '.join(keys) if keys else 'nenhuma'}")
    print(f"altura da base na pose inicial: {d.qpos[2]:.2f} m" if livres else "sem base flutuante")
    return 0


if __name__ == "__main__":
    sys.exit(main())
