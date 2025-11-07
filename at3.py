credito = print('escolha como deseja registrar suas transações:')
print('1 - crédito')
print('2 - debito')
print('3 - emprestimo')
print('4 - investimento')
print('5 - poupança')
responda = int(input('resposta:'))
if responda == 1:
    print('Saldo na conta: R$250')
    responda2 = int(input('qual o valor que deseja adicionar?'))
    responda2 = 250 + responda2
    print('valor final:', responda2)
if responda == 2:
     print('Saldo na conta: R$250')
     responda2 = int(input('qual o valor que deseja adicionar? '))
     responda2 = 250 + responda2 
     print('valor final:', responda2)
if responda == 3:
     print('saldo na conta: 250')
     responda2 = int(input('qual o valor do emprestimo? '))
     responda2 = 250. + responda2 
     print('valor da sua conta final', responda2)
     prestação = int(input('em quantos meses você irá pagar?'))
     prestação = responda2 * responda / prestação
     meses = prestação * (0.05) / 12 
     print('o valor que voce vai pagar é', prestação, 'mais 5% em juros')
     #QUE DEMONIO PQPPPPP
if responda == 4:
     print('saldo na conta: R$250')
     investimento = int(input('quanto que você gostaria de investir?'))
     meses = int(input('durante quantos meses você gostaria de ficar investindo?'))
     investimento = 250 - investimento 
     print('seu saldo final é de:', investimento)
     investimento = investimento + 1 * 12 
     print('seu saldo daqui', meses, 'será', investimento)
if responda == 5:
     print(' saldo na conta 250')
     poupança = int(input('qual o valor a adicionar na poupança?'))
     poupança = 250 + poupança
     print('feito, seu dinheiro esta guardado, o valor final de sua conta é', poupança)
     