F=${FTH:-$HOME/fth}; cd $F/anatomia && . $F/.venv/bin/activate
for k in 0 30 60 90 120; do
  echo "joelho $k°: $(python3 kit/torque_agachado.py --joelho $k | grep -E '^joelhos|^ATENÇÃO' | tr '\n' ' ')"
done
