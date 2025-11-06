altura = int(input('digite sua altura:'))
if altura <= 150:
    print('Ruim')
elif altura >= 151 and altura <= 160:
    print('aceitavel')
elif altura >= 161 and altura <= 165:
    print('bom')
elif altura >= 166 and altura <= 170:
    print('exelente')
elif altura >= 171 and altura <= 175:
    print('bom')
elif altura >= 176 and altura <= 180:
    print('aceitavel')
else:
    print('Ruim')

peso = int(input('digite seu peso:'))
if peso <= 45:
    print('ruim')
elif peso >= 46 and peso <= 55:
    print('bom')
elif peso >= 56 and peso <= 75:
    print('exelente')
elif peso >= 76 and peso <= 80:
    print('bom')
else:
    print('ruim')