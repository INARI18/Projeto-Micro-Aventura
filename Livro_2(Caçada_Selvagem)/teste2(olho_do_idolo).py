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

    tamanho = len(matriz)

    for i in range (tamanho):

        for j in range (tamanho):
            
            x = i - ((tamanho + 1) / 2) + 1
            y = j - ((tamanho + 1) / 2) + 1

            if (x**2 + y**2)**0.5 <= diametro/2:

                matriz[i][j] = caractere
    
    return matriz

def Mostra(matriz):

    tamanho = len(matriz)

    print()

    for i in range(tamanho):

        for j in range (tamanho):

            print(matriz[i][j], end='')

        print()

matriz = CriaTela(13)

matriz = Circulo(13, matriz, "@ ")
matriz = Circulo(11, matriz, ". ")
matriz = Circulo(5, matriz, "# ")

Mostra(matriz)