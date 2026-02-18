# #1
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def apresentar(self):
#         return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

#2

# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self, valor):
#         self.saldo += valor
#         return f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}."

#     def sacar(self, valor):
#         if valor > self.saldo:
#             return "Saldo insuficiente para saque."
#         else:
#             self.saldo -= valor
#             return f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}."
        
        
#3
# class produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco

#     def aplicar_desconto(self, percentual):
#         desconto = self.preco * (percentual / 100)
#         self.preco -= desconto
#         return f"Desconto de {percentual}% aplicado. Novo preço: R${self.preco:.2f}."
    


#4
# class retangulo:
#     def __init__(self, largura, altura):
#         self.largura = largura
#         self.altura = altura

#     def calcular_area(self):
#         return self.largura * self.altura

#     def calcular_perimetro(self):
#         return 2 * (self.largura + self.altura)
    
#5

# class carro:
#     def __init__(self, modelo, velocidade):
#         self.modelo = modelo
#         self.velocidade = velocidade
#     def acelerar(self, incremento):
#         self.velocidade += incremento
#         return f"O carro {self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h."
#     def frear(self, decremento):
#         self.velocidade -= decremento
#         if self.velocidade < 0:
#             self.velocidade = 0
#         return f"O carro {self.modelo} freou. Velocidade atual: {self.velocidade} km/h."
    
#6

# class aluno:
#     def __init__(self, nome, nota1, nota2):
#         self.nome = nome
#         self.nota1 = nota1
#         self.nota2 = nota2
#     def calcular_media(self):
#         media = (self.nota1 + self.nota2) / 2
#         return f"A média do aluno {self.nome} é: {media:.2f}."
#     def situacao(self):
#         media = (self.nota1 + self.nota2) / 2
#         if media >= 7:
#             return f"O aluno {self.nome} está aprovado."
#         elif media >= 5:
#             return f"O aluno {self.nome} está em recuperação."
#         else:
#             return f"O aluno {self.nome} está reprovado."

#7
# class lampada:
#     def __init__(self):
#         self.estado = "desligada"
#     def ligar(self):
#         self.estado = "ligada"
#         return f"A lâmpada está {self.estado}."
#     def desligar(self):
#         self.estado = "desligada"
#         return f"A lâmpada está {self.estado}."
#     def verificar_estado(self):
#         return f"A lâmpada está atualmente {self.estado}."


#8
# class Livro:
#     def __init__(self, titulo, autor, qtd):
#         self.titulo = titulo
#         self.autor = autor
#         self.qtd = qtd

#     def emprestar(self):
#         if self.qtd > 0:
#             self.qtd -= 1
#             return True
#         return False

#     def devolver(self):
#         self.qtd += 1


#9

# class termometro:
#     def __init__(self, celsius):
#         self.celsius = celsius
#     def celsius_para_fahrenheit(self):
#         fahrenheit = (self.celsius * 9/5) + 32
#         return f"{self.celsius}°C é igual a {fahrenheit:.2f}°F."
#     def fahrenheit_para_celsius(self, fahrenheit):
#         celsius = (fahrenheit - 32) * 5/9
#         return f"{fahrenheit}°F é igual a {celsius:.2f}°C."
#     def kelvin_para_celsius(self, kelvin):
#         celsius = kelvin - 273.15
#         return f"{kelvin}K é igual a {celsius:.2f}°C."
#     def celsius_para_kelvin(self):
#         kelvin = self.celsius + 273.15
#         return f"{self.celsius}°C é igual a {kelvin:.2f}K."

#10
# class televisao:
#     def __init__(self, canal=1, volume=10):
#         self.canal = canal
#         self.volume = volume

#     def mudar_canal(self, novo_canal):
#         self.canal = novo_canal
#         return f"Canal alterado para {self.canal}."

#     def aumentar_volume(self):
#         self.volume += 1
#         return f"Volume aumentado. Volume atual: {self.volume}."

#     def diminuir_volume(self):
#         if self.volume > 0:
#             self.volume -= 1
#             return f"Volume diminuído. Volume atual: {self.volume}."
#         else:
#             return "O volume já está no mínimo."
#     def mostrar_status(self):
#         return f"Televisão está no canal {self.canal} com volume {self.volume}."
    
#11
# class cronometro:
#     def __init__(self):
#         self.segundos = 0
#         self.minutos = 0
#         self.horas = 0

#     def iniciar(self):
#         return "Cronômetro iniciado."

#     def parar(self):
#         return "Cronômetro parado."

#     def resetar(self):
#         self.segundos = 0
#         self.minutos = 0
#         self.horas = 0
#         return "Cronômetro resetado."

#     def mostrar_tempo(self):
#         return f"Tempo atual: {self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}."
    
#12
class pedido:
    def __init__(self, lista_vazia_no_inicio):
        self.itens = lista_vazia_no_inicio
    def adicionar_item(self, nome, preço):
        self.itens.append({"nome": nome, "preço": preço})
        return f"Item '{nome}' adicionado ao pedido."
    def remover_item(self, nome, preco):
        for item in self.itens:
            if item["nome"] == nome and item["preço"] == preco:
                self.itens.remove(item)
                return f"Item '{nome}' removido do pedido."
        return f"Item '{nome}' não encontrado no pedido."
    def calcular_total(self):
        total = sum(item["preço"] for item in self.itens)
        return f"Total do pedido: R${total:.2f}."
    def mostrar_itens(self):
        if not self.itens:
            return "O pedido está vazio."
        itens_listados = "\n".join(f"{item['nome']}: R${item['preço']:.2f}" for item in self.itens)
        return f"Itens no pedido:\n{itens_listados}"    
    