#!/usr/bin/env python3
"""sensores.py — o que o G1 "sente" depois de 1 s parado em pé.

Uso: python3 kit/sensores.py [--segundos 1]
Lê os 4 sensores que o MJCF do Menagerie declara (giroscópio e acelerômetro na pelve e no tronco)
e ACRESCENTA, pela API MjSpec, três sensores que o arquivo não tem: orientação da IMU da pelve
(framequat) e força de 3 eixos no sítio de cada pé (force, como uma célula de carga no tornozelo).
Confere a força dos pés de dois jeitos: pelos sensores novos e somando os contatos com o chão.
"""
import argparse
import math
import sys

import mujoco
import numpy as np

import fth

MODELO = "unitree_g1/scene.xml"


def montar():
    spec = mujoco.MjSpec.from_file(str(fth.caminho(MODELO)))
    spec.add_sensor(name="orientacao_pelve", type=mujoco.mjtSensor.mjSENS_FRAMEQUAT,
                    objtype=mujoco.mjtObj.mjOBJ_SITE, objname="imu_in_pelvis")
    for lado, sitio in (("esq", "left_foot"), ("dir", "right_foot")):
        spec.add_sensor(name=f"forca_pe_{lado}", type=mujoco.mjtSensor.mjSENS_FORCE,
                        objtype=mujoco.mjtObj.mjOBJ_SITE, objname=sitio)
    return spec.compile()


def ler(m, d, nome):
    s = m.sensor(nome)
    return d.sensordata[s.adr[0]: s.adr[0] + s.dim[0]]


def rpy(q):
    w, x, y, z = q
    roll = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
    pitch = math.asin(max(-1.0, min(1.0, 2 * (w * y - z * x))))
    return math.degrees(roll), math.degrees(pitch)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--segundos", type=float, default=1.0)
    a = ap.parse_args()
    m = montar()
    d = mujoco.MjData(m)
    fth.pose_inicial(m, d)
    for _ in range(int(a.segundos / m.opt.timestep)):
        mujoco.mj_step(m, d)
    print(f"G1 parado {a.segundos:.0f} s · {m.nsensor} sensores (4 do arquivo + {m.nsensor - 4} acrescentados)")
    for nome in [m.sensor(i).name for i in range(m.nsensor)][:4]:
        v = ler(m, d, nome)
        print(f"  {nome:<34} {np.round(v, 1) + 0.0}")
    r, p = rpy(ler(m, d, "orientacao_pelve"))
    print(f"IMU (pelve): inclinação lateral {round(r, 1) + 0.0:.1f}° · frente/trás {round(p, 1) + 0.0:.1f}°")
    peso = sum(m.body_mass) * fth.G
    sens = {lado: float(np.linalg.norm(ler(m, d, f"forca_pe_{lado}"))) for lado in ("esq", "dir")}
    cont, _ = fth.forca_pes(m, d)
    c_esq, c_dir = cont["left_ankle_roll_link"], cont["right_ankle_roll_link"]
    print(f"sensor de força no tornozelo: pé esquerdo {sens['esq']:.0f} N · pé direito {sens['dir']:.0f} N")
    print(f"contatos com o chão:          pé esquerdo {c_esq:.0f} N · pé direito {c_dir:.0f} N")
    print(f"soma dos contatos / peso do robô ({peso:.0f} N): {(c_esq + c_dir) / peso:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
