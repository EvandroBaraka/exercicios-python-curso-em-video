valores = []

while True:
    num = int(input('Digite um número: '))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado. Não adicionado...')
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        print('Opção Inválida')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print('-=-' * 20)
print('Você digitou os valores ')
for c in valores:
    print(f'{c}... ', end='')
    