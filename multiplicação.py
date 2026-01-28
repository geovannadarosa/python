#a = [[1, 2],
#     [3, 4]]
#b = [[5, 6],
#     [7, 8]]
#resultado = [[0, 0],
#             [0, 0]]
#for i in range(len(a)):
#    for j in range (len(b[0])):
#        for k in range(len(b)):
#            resultado[i][j] += a[i][k] * b [k][j]
#print(resultado)

a = [
     [1, 2, 3],
     [4, 5, 6]
]
b = [
     [7, 8],
     [9, 10],
     [11, 12]
]
c = [
     [23, 24, 25, 26, 27],
     [28, 29, 30, 31, 32]
]
d = [
     [13, 14],
     [15, 16],
     [17, 18],
     [19, 20],
     [21, 22],
]
e = []
for i in range(2):
     linha = []
     for j in range(2):
           soma = 0
           for k in range(3):
               soma += a[i][k] * b[k][j]
           linha.append(soma)
     e.append(linha)     
print(e)

f = []
for i in range(2):
     linha = []
     for j in range(2):
           soma = 0
           for k in range(5):
               soma += c[i][k] * d[k][j]
           linha.append(soma)
     f.append(linha)     
print(f)
g = []
for i in range(2):
     linha = []
     for j in range(2):
          linha.append(e[i][j] + f[i][j])
     g.append(linha)
print(g)

          
