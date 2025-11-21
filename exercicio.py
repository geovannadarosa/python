from datetime import datetime

revistas = []
vendas = []

def cadastrar_revista():
    titulo = input("Digite o titulo da revista: ")
    categoria = input("Categoria (HQ, jornal, revista, etc..): ")
    try:
        preco = float(input("Preço: "))
    except ValueError:
        print("Preço inválido. Tente novamente.")
        return

    revistas.append({"titulo": titulo,
    "categoria": categoria,
    "preco": preco
    })

    print(f"Revista {titulo} cadastrada com sucesso.")

def registrar_venda():
    if not revistas:
        print("Nenhuma revista cadastrada ainda.")
        return
    
    titulo = input("Digite o titulo da revista: ")
    for revista in revistas:
        if revista["titulo"].lower() == titulo.lower():
            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida. Tente novamente.")
                return
            
            data = datetime.now().strftime("%d/%m/%Y")
            vendas.append({"titulo": titulo,
            "categoria": revista["categoria"],
            "preco": revista["preco"],
            "quantidade": quantidade,
            "data": data
            })
            print(f"Revista {titulo} vendida com sucesso.")
            
            return
    print(f"Revista {titulo} nao encontrada.")

def autoatendimento():
    if not revistas:
        print("Nenhuma revista cadastrada ainda.")
        return
    
    print("\nAutoatendimento")
    for i, r in enumerate(revistas, start=1):
        print(f"{i} - {r['titulo']} (R$ {r['preco']:.2f})")

    try:
        escolha = int(input("Escolha o número da revista: "))
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return

    if 1 <= escolha <= len(revistas):
        revista = revistas[escolha - 1]
        data = datetime.now().strftime("%d/%m/%Y")
        vendas.append({"titulo": revista["titulo"],
        "categoria": revista["categoria"],
        "preco": revista["preco"],
        "quantidade": quantidade,
        "data": data,
        "total": quantidade * revista["preco"]
        })
        print(f"Venda de {quantidade} revista(s) {revista['titulo']} realizada com sucesso.")
    else:
        print("Número inválido. Tente novamente.")
        return

def gerar_relatorio_diario():
    if not vendas:
        print("Nenhuma venda registrada ainda.")
        return
    
    data_desejada = input("Digite a data desejada (dd/mm/aaaa): ")

    total_vendas = 0
    print(f"\nRelatório Diário - {data_desejada}")
    for venda in vendas:
        if venda["data"] == data_desejada:
            print(f"Titulo: {venda['titulo']}")
            print(f"Categoria: {venda['categoria']}")
            print(f"Preço: R$ {venda['preco']:.2f}")
            print(f"Quantidade: {venda['quantidade']}")
            print(f"Data: {venda['data']}")
            print(f"Total: R$ {venda['total']:.2f}")
            print("-" * 30)
            total_vendas += venda["total"]
    
    print(f"Total de vendas: R$ {total_vendas:.2f}")
    print("-" * 30)

while True:
    print("\nMENU")
    print("1. Cadastrar revista")
    print("2. Registrar venda")
    print("3. Autoatendimento")
    print("4. Gerar relatório diário")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")

    match opcao:
        case "1":
            cadastrar_revista()
        case "2":
            registrar_venda()
        case "3":
            autoatendimento()
        case "4":
            gerar_relatorio_diario()
        case "0":
            break
        case _:
            print("Opção inválida. Tente novamente.")