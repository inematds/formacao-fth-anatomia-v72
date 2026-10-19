F=${FTH:-$HOME/fth}; cd $F/anatomia && . $F/.venv/bin/activate
python3 kit/autonomia.py --pack-s 13 --ah 9 --w 216     # G1: 9.000 mAh, 13S, ~2 h (unitree.com/g1)
python3 kit/autonomia.py --wh 972 --w 324               # H2: 0,972 kWh (unitree.com/H2)
python3 kit/autonomia.py --hz 1000 500 200 50 10        # orçamento de cada camada de controle
