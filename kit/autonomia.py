#!/usr/bin/env python3
"""autonomia.py — conta de bateria e de tempo de laço de um humanoide.

Uso: python3 kit/autonomia.py --wh ENERGIA_WH --w POTENCIA_MEDIA_W
     python3 kit/autonomia.py --pack-s CELULAS --ah AH [--v-celula 3.7] --w POTENCIA_MEDIA_W
     python3 kit/autonomia.py --hz 1000 500 50 10
Autonomia (min) = energia (Wh) / potência média (W) × 60. Sem margem de reserva: na vida real
ninguém descarrega a bateria até zero, então o tempo útil é menor.
Orçamento de laço = 1000 / frequência (ms): o tempo que cada camada tem para ler, calcular e mandar.
"""
import argparse
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wh", type=float, help="energia da bateria em Wh")
    ap.add_argument("--pack-s", type=int, help="células em série (ex.: 13 para 13S)")
    ap.add_argument("--ah", type=float, help="capacidade em Ah (9000 mAh = 9)")
    ap.add_argument("--v-celula", type=float, default=3.7, help="tensão nominal por célula (Li-ion: 3,6–3,7 V)")
    ap.add_argument("--w", type=float, help="potência média em W")
    ap.add_argument("--hz", type=float, nargs="+", help="frequências de laço para o orçamento de tempo")
    a = ap.parse_args()
    if a.hz:
        for f in a.hz:
            print(f"{f:>7.0f} Hz → {1000 / f:>6.1f} ms por ciclo")
        return 0
    if a.wh is None and a.pack_s and a.ah:
        v = a.pack_s * a.v_celula
        a.wh = v * a.ah
        print(f"pack {a.pack_s}S × {a.v_celula} V = {v:.1f} V nominal · {v:.1f} V × {a.ah:g} Ah = {a.wh:.0f} Wh (conta derivada)")
    if a.wh is None or not a.w:
        ap.print_help()
        return 2
    minutos = a.wh / a.w * 60
    print(f"energia {a.wh:.0f} Wh · potência média {a.w:.0f} W")
    print(f"autonomia: {minutos:.0f} min ({minutos / 60:.1f} h), sem reserva")
    return 0


if __name__ == "__main__":
    sys.exit(main())
