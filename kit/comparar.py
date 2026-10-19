#!/usr/bin/env python3
"""comparar.py — ficha técnica lida dos modelos MJCF, lado a lado.

Uso: python3 kit/comparar.py unitree_g1/scene.xml unitree_h1/scene.xml
Tudo sai do arquivo, não da propaganda: graus de liberdade acionados (nu), massa do modelo,
altura do centro de massa na pose inicial (1º keyframe ou pose zero), maior torque declarado
e quantos sensores o arquivo traz. Ficha do fabricante e modelo de simulação podem divergir:
a aula 8 ensina a anotar a diferença.
"""
import sys

import mujoco
import numpy as np

import fth


def ficha(arq):
    m = fth.carregar(arq)
    d = mujoco.MjData(m)
    fth.pose_inicial(m, d)
    art = fth.juntas_articuladas(m)
    lims = [(fth.limite_torque(m, j), fth.nome(m, mujoco.mjtObj.mjOBJ_JOINT, j)) for j in art]
    lims = [x for x in lims if not np.isnan(x[0])]
    tmax, jmax = max(lims) if lims else (float("nan"), "-")
    zmin = min(d.geom_xpos[g][2] for g in range(m.ngeom) if m.geom_bodyid[g] > 0)
    return {
        "GDL acionados (nu)": f"{m.nu}",
        "massa do modelo (kg)": f"{sum(m.body_mass):.1f}",
        "altura do CoM (m)": f"{d.subtree_com[1][2]:.2f}",
        "maior torque (N·m)": f"{tmax:.0f}",
        "junta do maior torque": jmax,
        "sensores no arquivo": f"{m.nsensor}",
        "pose inicial": fth.nome(m, mujoco.mjtObj.mjOBJ_KEY, 0) if m.nkey else "zero (sem keyframe)",
    }, zmin


def main():
    if len(sys.argv) < 3:
        print(__doc__.strip())
        return 2
    a, b = sys.argv[1], sys.argv[2]
    fa, _ = ficha(a)
    fb, _ = ficha(b)
    ca, cb = a.split("/")[0], b.split("/")[0]
    w = max(len(ca), len(cb), 20)
    print(f"{'item':<24} {ca:>{w}} {cb:>{w}}")
    for k in fa:
        print(f"{k:<24} {fa[k]:>{w}} {fb[k]:>{w}}")
    print(f"FICHA: {len(fa)} itens comparados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
