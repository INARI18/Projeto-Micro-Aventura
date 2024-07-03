#Analise de elementos

"""
RETRIUM = 3.3
HIDROGENIO = 12.8
DELIOS = 66.3
XENONIO = 71.7
RADONIO = 2.5
"""

import math

valor_elementos = [0.0]*5
nivel_elementos = 0.0
forca_devorim = 0.0
print()

elementos = ["RETRIUM", "HIDROGENIO", "DELIOS", "XENONIO", "RADONIO"]

for i in range (5):
    print(f"Qual eh o valor para {elementos[i]}: ")
    valor_elementos[i] = float(input())
print()
print("Quer ver a interpretacao? (SIM ou NAO)")
resposta = str(input().upper())
if (resposta == "SIM" or resposta == "S"):
    print("\n----------Resltado da Analise----------\n")
    for i in range (5):
        nivel_elementos = (13*abs(math.sin(math.radians(valor_elementos[i]))))
        print(f"{elementos[i]}: {round(nivel_elementos,3)}")
        if int(nivel_elementos) == 0:
            print("-")
        else:
            print("*" * int(nivel_elementos))
        if  nivel_elementos > 5:
            forca_devorim = nivel_elementos * 1.3 + forca_devorim
    print()
    if forca_devorim < 15:
        print("Voce esta seguro... Por enquanto")
        print("Forca Devorim em nivel:", round(forca_devorim,3))
    elif (forca_devorim > 15 and forca_devorim < 23):
        print("Voce esta em grave perigo!")
        print("Forca Devorim em nivel:", round(forca_devorim,3))
    elif forca_devorim >= 23:
        print("Voce esta prestes a morrer!")
        print("Forca Devorim em nivel:", round(forca_devorim,3))
else:
    print("Ok, mas voce vai se arrepender...")