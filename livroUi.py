from services.acoes import cadastrarlivro, mostrarLivros

def menu():
    while True:
        escolha = int(input('Escolha uma opção: '))
        match escolha:
            case 1:
                titulo = input('Titulo:') 
                autor = input('Autor: ')
                genero = input('genero: ')
                cadastrarlivro(titulo, autor, genero)
            
            case 2:
                mostrarLivros()
                
            case _:
                print('nada')
                break