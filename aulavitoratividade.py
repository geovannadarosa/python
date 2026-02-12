class animal:
    def __init__(self, nome, peso, raça):
        self.nome = nome
        self.peso = peso
        self.raça = raça
    
    def pular(self):
        print(f'o seu {self.raça} esta pulando')
    
    def voar(self):
        print(f'seu {self.raça} irá voar')
    def nadar(self):
        print(f'o seu {self.raça} está nadando')


