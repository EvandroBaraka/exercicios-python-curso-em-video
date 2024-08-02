# Faça um programa que leia uma ano e diga se ele é ou não bissexto

ano = int(input('Digite o ano que deseja saber se é bissexto: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print( 'O ano {} não é bissexto'.format(ano))