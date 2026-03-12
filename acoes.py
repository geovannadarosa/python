from domain.classe import Biblioteca

livros = []

def cadastrarlivro(titulo, autor, genero):
    l1 = Biblioteca(0, 0, 0)
    l1.setAutor = autor
    l1.setGenero = genero
    l1.setTitulo = titulo

    livros.append(l1)

def mostrarLivros():
    for livro in livros:
        print(livro)