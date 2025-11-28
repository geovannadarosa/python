salario = int(input('digite o valor do seu salario atual:'))
if salario == 280:
    print('aumento de 20%')
    atual = salario * 1.20 
    print(f'o valor do salario é {salario} \no porcentual de aumento é 20% \nvalor atual do salario é {atual}')
elif salario > 280 and salario <= 700:
    print('aumento de 15%')
    atual = salario * 1.15 
    print(f'o valor do salario é {salario} \no porcentual de aumento é 15% \nvalor atual do salario é {atual}')
elif salario > 700  and salario <= 1500:
    print('aumento de 10%')
    atual = salario * 1.10 
    print(f'o valor do salario é {salario} \no porcentual de aumento é 10% \nvalor atual do salario é {atual}')
else:
    print('aumento de 5%')
    atual = salario * 1.05 
    print(f'o valor do salario é {salario} \no porcentual de aumento é 5% \nvalor atual do salario é {atual}')
