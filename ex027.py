#Faça um programa que leia o nome completo de uma pessoa, e mostre em seguida seu primeiro e ultimo nomes separadamente.

nome = str(input('Digite seu nome completo: ')).upper().strip().split()

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome) - 1]))