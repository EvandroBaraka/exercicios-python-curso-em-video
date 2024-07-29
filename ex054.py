#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade a quantas já SÃO maiores.

from datetime import date
ano_atual = date.today().year

maiores = 0
menores = 0
print(ano_atual)
for c in range (1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if (ano_atual - ano) >= 18:
        maiores += 1
    else:
        menores += 1
print('{} destas pessoas já atingiram a maioridade, e {} pessoas ainda não.'.format(maiores, menores))
    