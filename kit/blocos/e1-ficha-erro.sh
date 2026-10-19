F=${FTH:-$HOME/fth}; cd $F
printf 'robo,estagio,fonte,data,evidencia\nTesla Optimus V3,em breve,vi num vídeo,2026,\n' > /tmp/ficha-erro.csv
python3 anatomia/kit/conferir_fichas.py /tmp/ficha-erro.csv; echo "saída: $?"
