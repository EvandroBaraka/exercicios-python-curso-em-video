from random import randint
from time import sleep

print('=' * 58)
print('Vou pensar em um número de 1 a 10 e você tenta adivinhar.')
print('=' * 58)
computador = randint(1, 10)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    tentativas += 1
    if jogador == computador:
        print('\n\033[32mCERTA RESPOSTA!!\033[m')
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente novamente.')
        elif jogador > computador:
            print('Menos... tente novamente.')
print('Você acertou com {} tentativas'.format(tentativas))