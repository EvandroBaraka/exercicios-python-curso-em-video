# crie um programa que leia o nome completo de uma pessoa, e mostre: 
# O nome com todas as letras maiúsculas 
# O nome com todas as letras minúsculas 
# Quantas letras ao todo (sem considerar espaços) 
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()

print('Maiúsculo: {}'.format(nome.upper()))
print('Minúsculo: {}'.format(nome.lower()))
print('Seu nome possui {} letras ao todo.'.format(len(nome) - nome.count(' ')))
nomes_separados = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nomes_separados[0], len(nomes_separados[0])))
input('\nPressione enter para finalizar.')