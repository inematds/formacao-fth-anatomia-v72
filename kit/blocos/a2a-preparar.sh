F=${FTH:-$HOME/fth}; mkdir -p $F && cd $F
python3.12 -m venv .venv && . .venv/bin/activate
pip install -q mujoco==3.16.0 numpy
[ -d anatomia ] || git clone -q --depth 1 https://github.com/inematds/formacao-fth-anatomia-v72 anatomia
[ -d mujoco_menagerie ] || git clone -q --filter=blob:none --sparse https://github.com/google-deepmind/mujoco_menagerie
cd mujoco_menagerie && git sparse-checkout set unitree_g1 unitree_h1 robotis_op3 booster_t1
git checkout -q 62ab00f && git log -1 --format='menagerie %h (%ad)' --date=short
python3 -c "import mujoco, numpy; print('mujoco', mujoco.__version__, '· numpy', numpy.__version__)"
