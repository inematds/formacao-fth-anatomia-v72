"""fth.py — funções comuns do kit do curso FTH 0 (O corpo do humanoide).

Acha o MuJoCo Menagerie em $FTH/mujoco_menagerie (padrão: a pasta acima do repositório do curso,
ou seja ~/fth/mujoco_menagerie) e carrega um modelo por caminho relativo ("unitree_g1/scene.xml").
Testado com mujoco 3.16.0 + numpy 2.x, Menagerie 62ab00f (15/10/2026), 19/10/2026.
"""
import os
import sys
from pathlib import Path

import mujoco
import numpy as np

KIT = Path(__file__).resolve().parent
RAIZ = Path(os.environ.get("FTH", KIT.parents[1]))
MENAGERIE = RAIZ / "mujoco_menagerie"
G = 9.81


def caminho(p):
    q = Path(p)
    if q.exists():
        return q
    r = MENAGERIE / p
    if r.exists():
        return r
    sys.exit(f"ERRO: não achei {p} (nem em {MENAGERIE}). Rode a preparação da aula 2.")


def carregar(p):
    return mujoco.MjModel.from_xml_path(str(caminho(p)))


def nome(m, tipo, i):
    return mujoco.mj_id2name(m, tipo, i) or f"#{i}"


def juntas_articuladas(m):
    """Índices das juntas de 1 grau (hinge/slide), sem a base flutuante."""
    return [j for j in range(m.njnt) if int(m.jnt_type[j]) in (int(mujoco.mjtJoint.mjJNT_HINGE), int(mujoco.mjtJoint.mjJNT_SLIDE))]


def limite_torque(m, j):
    """Torque máximo da junta j (N·m) declarado no MJCF: actuatorfrcrange da junta, forcerange ou ctrlrange do motor."""
    if m.jnt_actfrclimited[j]:
        return float(max(abs(m.jnt_actfrcrange[j][0]), abs(m.jnt_actfrcrange[j][1])))
    for a in range(m.nu):
        if m.actuator_trntype[a] == mujoco.mjtTrn.mjTRN_JOINT and m.actuator_trnid[a][0] == j:
            g = abs(m.actuator_gear[a][0])
            if m.actuator_forcelimited[a]:
                return float(max(abs(m.actuator_forcerange[a])) * g)
            if m.actuator_gaintype[a] == mujoco.mjtGain.mjGAIN_FIXED and m.actuator_biastype[a] == mujoco.mjtBias.mjBIAS_NONE:
                return float(max(abs(m.actuator_ctrlrange[a])) * g)  # motor de torque: ctrl já é torque
    return float("nan")


def pose_inicial(m, d):
    """Vai para o 1º keyframe (se existir) e copia o ctrl dele."""
    if m.nkey:
        mujoco.mj_resetDataKeyframe(m, d, 0)
    else:
        mujoco.mj_resetData(m, d)
    mujoco.mj_forward(m, d)


def corpo_do_geom(m, g):
    return nome(m, mujoco.mjtObj.mjOBJ_BODY, m.geom_bodyid[g])


def forca_pes(m, d, pes=("left_ankle_roll_link", "right_ankle_roll_link")):
    """Soma a força normal dos contatos de cada pé com o chão (N) e devolve também os pontos de contato."""
    soma = {p: 0.0 for p in pes}
    pontos = {p: [] for p in pes}
    f6 = np.zeros(6)
    for i in range(d.ncon):
        c = d.contact[i]
        for g in (c.geom1, c.geom2):
            b = corpo_do_geom(m, g)
            if b in soma:
                mujoco.mj_contactForce(m, d, i, f6)
                soma[b] += abs(f6[0])  # componente normal no referencial do contato
                pontos[b].append((c.pos[0], c.pos[1], abs(f6[0])))
    return soma, pontos
