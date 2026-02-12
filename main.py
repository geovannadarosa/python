# from aulavitor import pessoa

# nome = input('digite um nome:')
# idade = int(input('digite uma idade'))
# sexo = input('digite um sexo:')

# pessoa1 = pessoa(nome, idade, sexo)




from aulavitoratividade import animal
nome = input('digite o nome do seu animal: ')
peso = float(input('digite o peso do seu animal: '))
raça = input('digite a raça do seu animal')
animal1 = animal(nome, peso, raça)
while True:
    num = int(input('digite um numero para cada ação que seu animal deseja fazer: \n1 - pular \n2 - voar \n3 - nadar \n4 - sair'))
    if num == 1:
        animal.pular(animal1)
    elif num == 2:
        animal.voar(animal1)
    elif num == 3:
        animal.nadar(animal1)
    elif num == 4:
        print('nao se vaaaaaaaaaaaaaaaa...')
        break
    else:
        print('numero invalido')