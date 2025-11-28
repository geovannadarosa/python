nome = input('digite o nome:')
idade = int(input('digite sua idade:'))
if idade >= 0 and idade <= 2:
    print(f'o {nome} esta com a {idade} e ele é um bebê')
elif idade >= 3 and idade <= 11:
    print(f'o {nome} esta com a {idade} e ele é uma criança')
elif idade >= 12 and idade <= 21:
    print(f'o {nome} esta com a {idade} e ele é um jovem')
elif idade >= 22 and idade <= 64:
    print(f'o {nome} esta com a {idade} e ele é um Adulto')
elif idade >= 65 and idade <= 100:
    print(f'o {nome} esta com a {idade} e ele é um idoso')
else:
    print(f'o {nome} esta com a {idade} e ele é um muito velhinho')
