produto = {'nome':'laranja', 'preco':15, 'quantidade':3}
usuario = input('digite oque deseja consultar: \n nome, preço ou quantidade no estoque\n')
if usuario == 'nome':
    print(produto['nome'])
elif usuario == 'preco':
    print(produto['preco'])
elif usuario == 'quantidade no estoque':
    print(produto['quantidade'])
else:
    print('campo invalido')