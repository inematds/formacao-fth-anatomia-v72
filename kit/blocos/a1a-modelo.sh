F=${FTH:-$HOME/fth}; mkdir -p $F && cd $F
[ -d anatomia ] || git clone -q --depth 1 https://github.com/inematds/formacao-fth-anatomia-v72 anatomia
[ -f fichas.csv ] || cp anatomia/kit/fichas-modelo.csv fichas.csv   # sua cópia para preencher
python3 anatomia/kit/conferir_fichas.py anatomia/kit/fichas-modelo.csv; echo "saída: $?"
