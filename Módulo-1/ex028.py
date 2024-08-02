#Faça o computador pensar em um número, e peça para o usuário tentar adivinhar este número. Informe na tela se o usúario acertou ou errou.

from random import randint
from time import sleep
print('-=-' * 20)
print('Vou escolher um número de 1 a 5, e você tenta adivinhar.')
print('-=-' * 20)
n1 = int(randint(1, 5))
n2 = int(input('Digite o número de 1 a 5 que você acha que escolhi: '))
print('PROCESSANDO...')
sleep(2)
while n2 < 0 or n2 > 5 :
    n2 = int(input('Você digitou um número inválido, digite novamente: '))
    print('PROCESSANDO...')
    sleep(2)

if n1 == n2 :
    print('Parabéns, você acertou!!!')
else:
    print('Você errou!! Eu pensei no número {}'.format(n1))
input('')