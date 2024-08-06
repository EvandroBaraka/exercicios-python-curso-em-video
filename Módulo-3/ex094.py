pessoa = dict()
grupo = []
media = 0

while True:
    pessoa['Nome'] = str(input('Nome: ')).strip()
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. Digite apenas M ou F...')
    pessoa['Idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if continuar in 'SN':
            break
        print('ERRO. Digite apenas S ou N...')
    if continuar == 'N':
        break

for i in grupo:
    media += i['Idade']
media = media / len(grupo)

print('=*=' * 20)
print(f' - O grupo tem {len(grupo)} pessoas.')
print(f' - A média de idade do grupo é de {media:.2f} anos.')
print(f' - As mulheres cadastradas foram: ', end='')
for i in grupo:
    if i['sexo'] == 'F':
        print(i['Nome'], end=' - ')
print()
print(' - As pessoas com idade acima da média são: ')
print()
for i in grupo:
    if i['Idade'] > media:
        print(i)
        print()