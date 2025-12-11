def ler_notas():
    notas = []
    qtd = int(input("Quantas notas o aluno possui? "))
    
    for i in range(qtd):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    return notas
def calcular_media(lista_notas):
    soma = sum(lista_notas)
    media = soma / len(lista_notas)
    return media
def classificar(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"
def principal():
    notas = ler_notas()
    media = calcular_media(notas)
    situacao = classificar(media)

    print("\n--- RELATÓRIO ---")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")

principal()
