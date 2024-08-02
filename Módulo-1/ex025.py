# Crie um programa que leia o nome de uma pessoa, e diga se ela tem “Silva” no nome

nome = str(input('Digite o seu nome: ')).upper().strip()

print('O nome possui SILVA: {}'.format('SILVA' in nome))