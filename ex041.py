#A Confederação Nacional de Natação precisa de um programa que laia o ano de nascimento de um atleta a mostre sua categoria. da acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SENIOR
# Acima: MASTER

from datetime import date

ano_nasc = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')
