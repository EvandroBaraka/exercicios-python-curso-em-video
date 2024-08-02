# Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com o nome 'SANTO'

cidade = str(input('Digite o nome da cidade: ')).strip().upper().split()

print('A cidede começa com SANTO: ' 'SANTO' in cidade[0])