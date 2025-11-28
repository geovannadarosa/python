saldo = float(input('digite o saldo da sua conta atual:'))
debito = float(input('digite o valor do debito:'))
credito = float(input('digite o valor que foi creditado a sua conta:'))
saldo_atual = saldo - debito + credito 
if saldo_atual >= 1:
    print(f'o seu saldo atual é {saldo_atual} e ele é um saldo positivo')
else:
    print(f'saldo antigio {saldo} \n o valor debitado da sua conta é {debito} \n o valor creditado a sua conta é {credito} \n o seu saldo atual é {saldo_atual} e ele é um saldo negativo') 
    