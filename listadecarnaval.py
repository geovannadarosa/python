#1
# from defdecarnaval import Pessoa
# p1 = input("Digite o nome da pessoa: ")
# p2 = int(input("Digite a idade da pessoa: "))
# pessoa = Pessoa(p1, p2)
# print(pessoa.apresentar())
#2
# from defdecarnaval import ContaBancaria
# titular = input("Digite o nome do titular da conta: ")
# conta = ContaBancaria(titular, 0)
# print(f"Conta criada para o titular: {conta.titular}") 
# valor_deposito = float(input("Digite o valor a ser depositado: "))
# print(conta.depositar(valor_deposito))
# valor_saque = float(input("Digite o valor a ser sacado: "))
# print(conta.sacar(valor_saque)) 

#3
# from defdecarnaval import produto
# nome_produto = input("Digite o nome do produto: ")
# preco_produto = float(input("Digite o preço do produto: "))
# prod = produto(nome_produto, preco_produto)
# print(prod.aplicar_desconto(10))

#4
# from defdecarnaval import retangulo
# largura = float(input("Digite a largura do retângulo: "))
# altura = float(input("Digite a altura do retângulo: "))
# ret = retangulo(largura, altura)
# print(f"A área do retângulo é: {ret.calcular_area()}")
# print(f"O perímetro do retângulo é: {ret.calcular_perimetro()}")

#5
# from defdecarnaval import carro
# modelo_carro = input("Digite o modelo do carro: ")
# velocidade_inicial = float(input("Digite a velocidade inicial do carro (km/h): "))
# meu_carro = carro(modelo_carro, velocidade_inicial)
# incremento = float(input("Digite o valor de incremento para acelerar (km/h): "))
# print(meu_carro.acelerar(incremento))
# decremento = float(input("Digite o valor de decremento para frear (km/h): "))
# print(meu_carro.frear(decremento))

#6
# from defdecarnaval import aluno
# nome_aluno = input("Digite o nome do aluno: ")
# nota1 = float(input("Digite a primeira nota do aluno: "))
# nota2 = float(input("Digite a segunda nota do aluno: "))
# aluno1 = aluno(nome_aluno, nota1, nota2)
# print(aluno1.calcular_media())
# print(aluno1.situacao())
# for i in range(1, 6, 3):
#     print(f"Aluno {i}:")
#     nome_aluno = input("Digite o nome do aluno: ")
#     nota1 = float(input("Digite a primeira nota do aluno: "))
#     nota2 = float(input("Digite a segunda nota do aluno: "))
#     aluno_i = aluno(nome_aluno, nota1, nota2)
#     print(aluno_i.calcular_media())
#     print(aluno_i.situacao())

# #7
# from defdecarnaval import lampada
# ligar = input("Deseja ligar a lampada digite 1 \nSe deseja desligar digite 2\n")
# lampada1 = lampada()
# for i in range(1, 6):
#     print(f"Lampada {i}:")
#     ligar = input("Deseja ligar a lampada digite 1 \nSe deseja desligar digite 2\n")
#     lampada_i = lampada()
#     if ligar == "1":
#         print(lampada_i.ligar())
#     elif ligar == "2":
#         print(lampada_i.desligar())
#     else:
#         print("Opção inválida.")
#     print(f"A lampada está atualmente: {lampada_i.verificar_estado()}")

#8
# from defdecarnaval import Livro

# def main():
#     livro = Livro("Dom Casmurro", "Machado de Assis", 3)

#     print(f"Livro: {livro.titulo} - Quantidade inicial: {livro.qtd}\n")

#     while True:
#         if livro.emprestar():
#             print(f"Empréstimo realizado! Quantidade restante: {livro.qtd}")
#         else:
#             print("Não há mais exemplares disponíveis.")
#             break

#     print("\nDevolvendo um livro...")
#     livro.devolver()
#     print(f"Quantidade após devolução: {livro.qtd}")

#     print("\nTentando emprestar novamente...")
#     if livro.emprestar():
#         print(f"Empréstimo realizado! Quantidade restante: {livro.qtd}")
#     else:
#         print("Não há mais exemplares disponíveis.")



# if __name__ == "__main__":
#     main()

#9

# from defdecarnaval import termometro
# celsius = float(input("Digite a temperatura em Celsius: "))
# termometro1 = termometro(celsius)
# print(f"A temperatura em Fahrenheit é: {termometro1.celsius * 9/5 + 32:.2f} °F")
# fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))   
# print(f"A temperatura em Celsius é: {(fahrenheit - 32) * 5/9:.2f} °C")
# kelvin = float(input("Digite a temperatura em Kelvin: "))
# print(f"A temperatura em Celsius é: {kelvin - 273.15:.2f} °C")

#10
# from defdecarnaval import televisao
# mudar_canal = input("Deseja mudar o canal? (sim/não): ")
# tv1 = televisao()
# if mudar_canal.lower() == "sim":
#     novo_canal = int(input("Digite o novo canal: "))
#     print(tv1.mudar_canal(novo_canal))
# print(tv1.mostrar_status())
# aumentar_volume = input("Deseja aumentar o volume? (sim/não): ")
# if aumentar_volume.lower() == "sim":
#     tv1.aumentar_volume()
# print(tv1.mostrar_status())

#11
# from defdecarnaval import cronometro
# cronometro1 = cronometro()
# while True:
#     acao = input("Digite 'start' para iniciar, 'stop' para parar ou 'reset' para reiniciar o cronômetro: ").lower()
#     if acao == "start":
#         print(cronometro1.iniciar())
#     elif acao == "stop":
#         print(cronometro1.parar())
#     elif acao == "reset":
#         print(cronometro1.resetar())
#     else:
#         print("Ação inválida. Por favor, digite 'start', 'stop' ou 'reset'.")

#12
from defdecarnaval import pedido
pedido1 = pedido()
while True:
    acao = input("Digite 'adicionar' para adicionar um item, 'remover' para remover um item ou 'finalizar' para finalizar o pedido: ").lower()
    if acao == "adicionar":
        item = input("Digite o nome do item a ser adicionado: ")
        print(pedido1.adicionar_item(item))
    elif acao == "remover":
        item = input("Digite o nome do item a ser removido: ")
        print(pedido1.remover_item(item))
    elif acao == "finalizar":
        print(pedido1.finalizar_pedido())
        break
    else:
        print("Ação inválida. Por favor, digite 'adicionar', 'remover' ou 'finalizar'.")
    