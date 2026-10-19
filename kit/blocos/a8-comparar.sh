F=${FTH:-$HOME/fth}; cd $F/anatomia && . $F/.venv/bin/activate
python3 kit/comparar.py unitree_g1/scene.xml unitree_h1/scene.xml; echo "saída: $?"
