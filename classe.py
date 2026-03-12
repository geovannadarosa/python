class Biblioteca:
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    @property
    def getTitulo(self):
        return self._titulo
    @getTitulo.setter
    def setTitulo(self, nome):
        self._titulo = nome

    @property
    def getAutor(self):
        return self._autor
    @getTitulo.setter
    def setAutor(self, nome):
        self._autor = nome

    @property
    def getGenero(self):
        return self._genero
    @getGenero.setter
    def setGenero(self, nome):
        self._genero = nome
