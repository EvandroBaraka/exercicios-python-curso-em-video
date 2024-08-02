t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
quantidade = int(input('Digite quantos termos quer vizualizar: '))
total = t + r * quantidade
print('Os {} primeiros termos da PA são: '.format(quantidade))
while t < total:
    print('{}'.format(t), end=' > ')
    t += r
print('FIM')