#altura do olho: 6.5
#altura do coracao: 3.25
#distancia da base: 4.5

from random import randint
from math import atan, pi

print("Reflexao do Feixe")
print("-----------------")
print("Qual a altura do olho do Idolo?")
altura_olho = float(input())
print("Qual a altura do coracao do Idolo?")
altura_coracao = float(input())
print("Qual a sua distancia da base do Idolo?")
distancia_base = float(input())

W = randint(2, 5)

while 1:

    print("Angulo de ajuste do espelho (em graus): ")
    angulo_espelho = int(input())

    A = atan(altura_coracao / distancia_base)
    B = atan(altura_olho / distancia_base)
    B2 = (B - A) / 2
    C = (pi / 2) - B2
    D = pi - B - C
    D = D * (180 / pi)

    if abs(D - angulo_espelho) > W:

        print("O Idolo foi destruido!")
        break

    else:

        print(f"Voce errou por {int(abs(D - 7))} graus")
        print("\nSe voce ainda esta vivo, tente de novo!\n")
