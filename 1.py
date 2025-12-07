idade = int(input('digite sua idade:'))
if idade >= 0 and idade <= 11:
    print(f'você tem {idade} e você é uma criança')
elif idade >= 12 and idade <= 17:
    print(f'você tem {idade} e você é um adolescente')
elif idade >= 18 and idade <= 59:
    print(f'você tem {idade} e você é um adulto')
elif idade >= 60 and idade <= 120:
    print(f'você tem {idade} e você é um idoso')
else:
    print(f'idade invalida')
