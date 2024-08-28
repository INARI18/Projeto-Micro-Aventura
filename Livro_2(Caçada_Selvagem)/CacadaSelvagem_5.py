#altura do olho: 6.5
#altura do coracao: 3.25
#distancia da base: 4.5

from random import randint
from math import atan, degrees

print("Reflexao do Feixe")
print("-----------------")
print("Qual a altura do olho do Idolo?")
altura_olho = float(input())
print("Qual a altura do coracao do Idolo?")
altura_coracao = float(input())
print("Qual a sua distancia da base do Idolo?")
distancia_base = float(input())

margem_erro = randint(2, 4)

while 1:

    print("Angulo de ajuste do espelho (em graus): ")
    angulo_espelho = int(input())

    angulo_maior = atan(altura_coracao / distancia_base)
    angulo_menor = atan(altura_olho / distancia_base)
    angulo_menor = degrees(angulo_menor)
    angulo_maior = degrees(angulo_maior)

    angulo_diferenca = angulo_maior - angulo_menor
    angulo_reflexao = angulo_menor + angulo_diferenca / 2

    diferenca = angulo_reflexao - angulo_espelho

    if abs(diferenca) <= margem_erro:

        print("\nO Idolo foi destruido!")
        break

    elif diferenca > 0:

        print("\nMuito baixo! Voce errou o alvo!")

    elif diferenca < 0:

        print("\nMuito alto! Voce errou o alvo!")

    print("Se voce ainda esta vivo, tente de novo!\n")