#Analise de Elementos

"""
RETRIUM = 3.3
HIDROGENIO = 12.8
DELIOS = 66.3
XENONIO = 71.7
RADONIO = 2.5
"""

import math

VALOR_ELEMENTOS = [0.0]*5
NIVEL_ELEMENTOS = 0.0
FORCA_DEVORIM = 0.0
print()

ELEMENTOS = ["RETRIUM", "HIDROGENIO", "DELIOS", "XENONIO", "RADONIO"]

for i in range (5):
    print(f"Qual eh o valor para {ELEMENTOS[i]}: ")
    VALOR_ELEMENTOS[i] = float(input())
print()
print("Quer ver a interpretacao? (SIM ou NAO)")
RESPOSTA = str(input().upper())
if (RESPOSTA == "SIM" or RESPOSTA == "S"):
    print("----------Resltado da Analise----------")
    for i in range (5):
        NIVEL_ELEMENTOS = (13*abs(math.sin(math.radians(VALOR_ELEMENTOS[i]))))
        print(f"{ELEMENTOS[i]}: {round(NIVEL_ELEMENTOS,3)}")
        if int(NIVEL_ELEMENTOS) == 0:
            print("-")
        else:
            print("*" * int(NIVEL_ELEMENTOS))
        if  NIVEL_ELEMENTOS > 5:
            FORCA_DEVORIM = NIVEL_ELEMENTOS * 1.3 + FORCA_DEVORIM
    print()
    if FORCA_DEVORIM < 15:
        print("Voce esta seguro... Por enquanto")
        print("Forca Devorim em nivel:", round(FORCA_DEVORIM,3))
    if (FORCA_DEVORIM > 15 and FORCA_DEVORIM < 23):
        print("Voce esta em grave perigo!")
        print("Forca Devorim em nivel:", round(FORCA_DEVORIM,3))
    if FORCA_DEVORIM >= 23:
        print("Voce esta prestes a morrer!")
        print("Forca Devorim em nivel:", round(FORCA_DEVORIM,3))
else:
    print("Ok, mas voce vai se arrepender...")