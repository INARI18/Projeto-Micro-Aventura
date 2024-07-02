#Olho do Idolo

def CriaTela(linhas, colunas):

    matriz = []

    for i in range (linhas):
        linha = []
        
        for j in range (colunas):
            linha.append(0)
        
        matriz.append(linha)
    
    return matriz

matriz = CriaTela(10, 10)

for i in matriz:
    print(i)