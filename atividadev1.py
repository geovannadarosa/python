idade = int(input('digite um numero:'))
try:
    if idade <= 11:
        print('criança')
    elif idade >= 12 and idade <= 17:
        print('adolescente')
    elif idade >= 18 and idade <= 59:
        print('adulto')
    elif idade >= 60 and idade <= 120:
        print('idoso')
    else:
        raise ValueError
except ValueError:
    print(f"Erro, você digitou uma idade invalida")