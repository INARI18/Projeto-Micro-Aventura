#Olho do Idolo

def CriaTela(tamanho):

    matriz = []

    for i in range (tamanho):
        linha = []
        
        for j in range (tamanho):
            linha.append("  ")

        matriz.append(linha)
    
    return matriz

def Circulo(diametro, matriz, caractere):

    contador = 0

    for linha in matriz:

        for coluna in range (25):
            
            coordenada_x = contador - 13 + 1
            coordenada_y = coluna - 13 + 1

            if (coordenada_x**2 + coordenada_y**2)**0.5 <= diametro/2:

                linha[coluna] = caractere

        contador += 1
    
    return matriz

matriz = CriaTela(25)

matriz = Circulo(25, matriz, "# ")
matriz = Circulo(19, matriz, ". ")
matriz = Circulo(11, matriz, "0 ")

print()

for i in matriz:

    for j in range (25):

        print(i[j], end='')

    print()