#!/usr/bin/env python3
"""conferir_fichas.py — confere a tabela de humanoides da aula 1: estágio, fonte e data em toda linha.

Uso: python3 kit/conferir_fichas.py fichas.csv
Colunas: robo,estagio,fonte,data,evidencia
  estagio  = demo | piloto | produção   (demo: só vídeo/evento; piloto: em cliente, tarefa estreita;
             produção: vendido ou entregue em série a quem paga)
  fonte    = URL https:// da fonte que sustenta o estágio
  data     = quando a fonte foi publicada ou lida: DD/MM/AAAA ou MM/AAAA
Sai com código 0 só se houver 6 robôs ou mais e todos tiverem estágio, fonte e data válidos.
"""
import csv
import re
import sys

ESTAGIOS = {"demo": "demo", "piloto": "piloto", "produção": "produção", "producao": "produção"}
DATA = re.compile(r"^(\d{2}/)?\d{2}/\d{4}$")


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 2
    with open(sys.argv[1], encoding="utf-8") as f:
        linhas = [r for r in csv.DictReader(f) if (r.get("robo") or "").strip()]
    ok = 0
    contagem = {"demo": 0, "piloto": 0, "produção": 0}
    for r in linhas:
        falta = []
        est = ESTAGIOS.get((r.get("estagio") or "").strip().lower())
        if not est:
            falta.append("estágio")
        if not (r.get("fonte") or "").strip().startswith("https://"):
            falta.append("fonte")
        if not DATA.match((r.get("data") or "").strip()):
            falta.append("data")
        if falta:
            print(f"  {r['robo'].strip():<22} falta: {', '.join(falta)}")
        else:
            ok += 1
            contagem[est] += 1
            print(f"  {r['robo'].strip():<22} {est:<9} {r['data'].strip()}")
    print(f"estágios: demo {contagem['demo']} · piloto {contagem['piloto']} · produção {contagem['produção']}")
    print(f"{len(linhas)} robôs, {ok} com fonte e data")
    return 0 if len(linhas) >= 6 and ok == len(linhas) else 1


if __name__ == "__main__":
    sys.exit(main())
