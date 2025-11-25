

entradas = []
saidas = []
saldo = 0.0

def registrar_entrada():
    global saldo
    tipo = input("Tipo de entrada (salário, investimento, outras rendas): ")
    valor = float(input("Valor da entrada: R$ "))
    data = input("Data da entrada (dd/mm/aaaa): ")

    entradas.append({"tipo": tipo, "valor": valor, "data": data})
    saldo += valor
    print("Entrada registrada com sucesso!\n")


def registrar_saida():
    global saldo
    tipo = input("Tipo de saída (contas fixas, compras, serviços): ")
    valor = float(input("Valor da saída: R$ "))
    data = input("Data da saída (dd/mm/aaaa): ")

    
    if valor > saldo:
        print("Erro! A saída não pode ser maior que o saldo disponível.")
        return

   
    saidas.append({"tipo": tipo, "valor": valor, "data": data})
    saldo -= valor
    print("Saída registrada com sucesso!\n")


def mostrar_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}\n")


def relatorio_mensal():
    total_entradas = sum(e["valor"] for e in entradas)
    total_saidas = sum(s["valor"] for s in saidas)
    saldo_final = total_entradas - total_saidas

    print("\n===== RELATÓRIO MENSAL =====")
    print(f"Total de entradas: R$ {total_entradas:.2f}")
    print(f"Total de saídas: R$ {total_saidas:.2f}")
    print(f"Saldo final: R$ {saldo_final:.2f}")
    print("=============================\n")


while True:
    print("===== SISTEMA FINANCEIRO =====")
    print("1 - Registrar entrada")
    print("2 - Registrar saída")
    print("3 - Mostrar saldo atual")
    print("4 - Gerar relatório mensal")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_entrada()
    elif opcao == "2":
        registrar_saida()
    elif opcao == "3":
        mostrar_saldo()
    elif opcao == "4":
        relatorio_mensal()
    elif opcao == "0":
        print("Encerrando sistema...")
        break
    else:
        print("Opção inválida!\n")
