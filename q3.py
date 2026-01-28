linha = int(input('digite a quantidade de linhas na matriz:'))
coluna = int(input('digite a quantidade de colunas na matriz:'))
matriz = []
for i in range(linha):
    linha = []
    for j in range(coluna):
        linha.append(int(input('digite os valores da matriz:')))
    matriz.append(linha)
print(matriz)