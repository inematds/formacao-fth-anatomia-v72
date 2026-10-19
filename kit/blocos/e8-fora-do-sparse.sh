F=${FTH:-$HOME/fth}; cd $F/anatomia && . $F/.venv/bin/activate
python3 kit/comparar.py unitree_g1/scene.xml apptronik_apollo/scene.xml; echo "saída: $?"
