galera = list()
pessoa = list()
peso = []
maiores = []
menores = []
print('=*=' * 10)
print('{:^30}'.format('Cadastro de Candidatos'))
print('=*=' * 10)
while True:
    pessoa.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    continuar = input('Continuar [S/N]: ')
    if continuar in 'Nn':
        break
galera.append(pessoa[:])
galera.append(peso[:])
for i, p in enumerate(galera[1]):
    if p == max(galera[1]):
        maiores.append(galera[0][i])
    if p == min(galera[1]):
        menores.append(galera[0][i])
print('-=-' * 20)
print(f'Foram cadastradas {len(galera[0])} pessoas.')
print(f'O maior peso registrado foi {max(galera[1])}kg. Peso de {maiores}')
print(f'O menor peso registrado foi {min(galera[1])}kg. Peso de {menores}')