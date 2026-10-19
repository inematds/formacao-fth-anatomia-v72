#!/usr/bin/env python3
"""juntas.py — árvore de juntas de um humanoide lida do MJCF, com limites em graus e torque máximo.

Uso: python3 kit/juntas.py [modelo]   (padrão: unitree_g1/scene.xml)
A indentação segue a árvore de corpos: cada nível é um elo pendurado no anterior.
"""
import math
import sys

import mujoco

import fth


def profundidade(m, b):
    n = 0
    while b > 0:
        b = m.body_parentid[b]
        n += 1
    return n


def main():
    arq = sys.argv[1] if len(sys.argv) > 1 else "unitree_g1/scene.xml"
    m = fth.carregar(arq)
    art = fth.juntas_articuladas(m)
    livres = [j for j in range(m.njnt) if m.jnt_type[j] == mujoco.mjtJoint.mjJNT_FREE]
    print(f"{arq} · {len(art)} juntas articuladas")
    print(f"{'junta':<42} {'mín°':>6} {'máx°':>6} {'torque máx (N·m)':>17}")
    for j in art:
        b = m.jnt_bodyid[j]
        ind = "  " * (profundidade(m, b) - 1)
        lo, hi = (math.degrees(x) for x in m.jnt_range[j]) if m.jnt_limited[j] else (float("-inf"), float("inf"))
        tq = fth.limite_torque(m, j)
        print(f"{(ind + fth.nome(m, mujoco.mjtObj.mjOBJ_JOINT, j)):<42} {lo:>6.0f} {hi:>6.0f} {tq:>17.0f}")
    bate = "sim" if len(art) == m.nu else "não"
    print(f"RESUMO: {len(art)} juntas articuladas + {len(livres)} base flutuante · nu={m.nu} · bate com nu: {bate}")
    return 0 if bate == "sim" else 1


if __name__ == "__main__":
    sys.exit(main())
