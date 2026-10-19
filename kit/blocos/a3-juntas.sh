F=${FTH:-$HOME/fth}; cd $F/anatomia && . $F/.venv/bin/activate
python3 kit/juntas.py unitree_g1/scene.xml; echo "saída: $?"
