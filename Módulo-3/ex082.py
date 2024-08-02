completa = list()
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    completa.append(num)
    opcao = str(input('Deseja continuar? [S/N] '))
    while opcao not in 'SsNn':
        opcao = str(input('Deseja continuar? [S/N] '))
    if opcao in 'Nn':
        break
for c in completa:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'\nA lista de números digitados foi {completa}')
print(f'Os números ímpares são {impares}')
print(f'Os números pares são {pares}')
