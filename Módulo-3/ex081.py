numeros = list()
quantidade = 0
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    quantidade += 1
    print('Número adicionado a lista...')
    resposta = str(input('Deseja continuar? [S/N] '))
    while resposta not in 'SsNn':
        resposta = str(input('Deseja continuar? [S/N] '))
    if resposta in 'Nn':
        break
numeros.sort(reverse=True)
print(f'\nForam digitados {quantidade} números...')
print(f'Os números em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O número 5 foi digitado e se encontra na posição ', end='')
    for i, c in enumerate(numeros):
        if c == 5:
            print(f'{i}... ', end='')
else:
    print('O número 5 não foi encontrado na lista.')
    