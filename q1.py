matriz = [[1, 2],
          [3, 4]]
matriz2 = [[5, 6],
           [7, 8]]
final = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(matriz[i][j] + matriz2[i][j])
    final.append(linha)
print(final)