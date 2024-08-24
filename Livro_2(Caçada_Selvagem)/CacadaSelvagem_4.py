"""
PASSAGEM 1: 16 25 30 27 12 17 10 7 4 
PASSAGEM 2: 44 29 42 31 8 21 6 15 11
PASSAGEM 3: 16 25 22 35 8 26 7 14 23
PASSAGEM 4: 24 33 14 27 4 17 22 17 8
"""

direcoes = [0]*4
cardiais = ["N", "S", "L", "O"]
numeros_usuario = [0]*9


print("Qual passagem? (1 a 4)")
passagem = int(input())

print("Digite a sequencia de 9 numeros (um de cada vez): ")
for i in range (9):
    print(f"{i+1}: ", end='')
    resposta = int(input())
    numeros_usuario[i] = resposta

print()
print(f"Passagem {passagem}: ")

for i in numeros_usuario:
    calculo_direcao = int(i / 4)
    cardial = (i - calculo_direcao * 4)
    direcoes[cardial] += calculo_direcao
    print(f"{calculo_direcao} -> {cardiais[cardial]}")

print("\n----------------------\n")

if (direcoes[0] == direcoes[1] and direcoes[2] == direcoes[3]):
    print(f"A passagem {passagem} leva ao segredo do Idolo")
else:
    print(f"A passagem {passagem} leva a MORTE!")