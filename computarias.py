livros = []

def cadastrar_livro():
    if len(livros) >= 100:
        print("Limite de livros atingido.")
        return
    
    nome = str(input("Nome do livro: "))
    autor = str(input("Autor do livro: "))
    genero = str(input("Gênero do livro: "))
    ano = input("Ano de publicação: ")

    livros.append({
        "nome": nome,
        "autor": autor,
        "genero": genero,
        "ano": ano
    })

    print(f"Livro {nome} cadastrado com sucesso.\n")

def buscar_campo(campo):
    termo = input(f"Digite o {campo} para buscar: ").lower()
    encontrados = [livro for livro in livros if livro[campo].lower() == termo]

    if encontrados:
        print("Livros encontrados:")
        for livro in encontrados:
            print(f"Nome: {livro['nome']}, Autor: {livro['autor']}, Gênero: {livro['genero']}, Ano: {livro['ano']}")
    else:
        print("Nenhum livro encontrado.")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("\nTODOS OS LIVROS")
        for i, livro in enumerate(livros, start=1):
            print(f"Livro {i}: {livro['nome']}")
            for chave, valor in livro.items():
                print(f"{chave.capitalize()}: {valor}")
            print("-" * 30)

def marcar_lido():
    nome = str(input("Digite o nome do livro: ")).lower()
    for livro in livros:
        if livro["nome"].lower() == nome:
            livro["status"] = "lido"
            print(f"Livro {nome} marcado como lido.")
            return
    print(f"Livro {nome} nao encontrado.")

while True:
    print("\nMENU")
    print("1. Cadastrar livro")
    print("2. Buscar por nome")
    print("3. Buscar por autor")
    print("4. Buscar por gênero")
    print("5. Listar todos os livros")
    print("6. Marcar livro como lido")
    print("0. Sair")
    opcao = input("Digite a opção desejada: ")

    match opcao:
        case "1":
            cadastrar_livro()
        case "2":
            buscar_campo("nome")
        case "3":
            buscar_campo("autor")
        case "4":
            buscar_campo("genero")
        case "5":
            listar_livros()
        case "6":
            marcar_lido()
        case "0":
            break
        case _:
            print("Opção inválida. Tente novamente.")
