#Olho do Idolo

def CriaTela(linhas, colunas):

    matriz = []

    for i in range (linhas):
        linha = []
        
        for j in range (colunas):
            linha.append("  ")

        matriz.append(linha)
    
    return matriz

def Circulo(diametro, matriz, caractere):

    ii = 0

    for i in matriz:

        for j in range (25):
            
            x = ii - 13 + 1
            y = j - 13 + 1

            if (x**2 + y**2)**0.5 <= diametro/2:

                i[j] = caractere

        ii += 1
    
    return matriz

matriz = CriaTela(25, 25)

matriz = Circulo(15, matriz, "@ ")
matriz = Circulo(13, matriz, "  ")
matriz = Circulo(7, matriz, "# ")

print()

for i in matriz:

    for j in range (25):

        print(i[j], end='')

    print()