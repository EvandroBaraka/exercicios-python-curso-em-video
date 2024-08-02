# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a idade dele:
# - Se ele ainda vai se alistar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar quanto que falta ou que passou do prazo.

from datetime import date

print('\033[1;33m===' * 16)
print('PROGRAMA DE VERIFICAÇÃO DE IDADE DE ALISTAMENTO.')
print('===' * 16)
print('\033[m')

ano_atual = date.today().year

ano_usuario = int(input('Digite seu ano de nascimento: '))

idade = ano_atual - ano_usuario

print('Você tem {} anos.'.format(idade))
if idade < 18:
    print('Você deverá se alistar para o serviço militar daqui {} ano(s).'.format(18 - idade))
elif idade == 18:
    print('Já está na hora de se alistar.')
elif idade > 18:
    print('Já passaram {} anos do seu periodo de alistamento.'.format(idade - 18))