matriz = []
for i in range(1):
    linha = []
    for j in range(3):
        if j == 0:
            linha.append(input('digite o seu nome:'))
        elif j == 1:
            linha.append(input('digite o seu telefone:'))
        else:
            linha.append(input('digite sua idade:'))
    matriz.append(linha)
print(matriz)
            