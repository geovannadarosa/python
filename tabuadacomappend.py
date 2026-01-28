matriz = []

print(matriz)
for i in range(6):
    linha = []
    for j in range(6):
        if i == 0:
            linha.append(j)
        elif j == 0:
            linha.append(i)
        else:
            linha.append(j * i)
    matriz.append(linha)
for i in range(6):
    for j in range(6):
        print(matriz[i][j], end= ' ')
    print('\n')
