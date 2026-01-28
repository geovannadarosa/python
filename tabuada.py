matriz = [
    [0, 1, 2, 3, 4, 5],
    [1, 1, 2, 3, 4, 5],
    [2, 2, 4, 6, 8, 10],
    [3, 3, 6, 9, 12, 15],
    [4, 4, 8, 12, 16, 20],
    [5, 5, 10, 15, 20, 25]
]

print(matriz)
for i in range(6):
    for j in range(6):
        print(matriz[i][j], end=' ')
    print('\n')  