F=${FTH:-$HOME/fth}; cd $F/anatomia && . $F/.venv/bin/activate
for r in unitree_h1 robotis_op3 booster_t1; do
  echo "$r: $(python3 kit/abrir.py $r/scene.xml | sed -n 2p)"
done
