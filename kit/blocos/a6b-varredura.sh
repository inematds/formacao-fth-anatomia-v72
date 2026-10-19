F=${FTH:-$HOME/fth}; cd $F/anatomia && . $F/.venv/bin/activate
for n in 10 15 20 25 30 35 40; do
  echo "$n N → $(python3 kit/equilibrio.py --empurrao $n | tail -2 | cut -d'(' -f1 | tr '\n' ' ')"
done
