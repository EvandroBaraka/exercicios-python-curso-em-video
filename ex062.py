print('-=-' * 5)
print('GERADOR DE PA')
print('-=-' * 5)
t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão: '))
total = t + r * 10
print('Os 10 primeiros termos da PA são: ')

while t < total:
    while t < total:
        print('{}'.format(t), end=' > ')
        t += r
    print('PAUSA')
    quantidade = int(input('Deseja visualizar mais quantos termos: '))
    total = t + r * quantidade
print('ENCERRANDO...')