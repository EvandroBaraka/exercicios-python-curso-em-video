from random import randint
from time import sleep
print('=' * 30)
print('Vou pensar em um número de 1 a 10 e você tenta adivinhar.')
print('=' * 30)
num_pc = int(randint(1, 10))
num_user = int(input('Digite o número: '))
print('PROCESSANDO...')
sleep(1)
tentativas = 1

while num_pc != num_user:
    print('\n\033[31mERROU!\033[m')
    num_user = int(input('Tente novamente: '))
    print('PROCESSANDO...')
    sleep(1)
    tentativas += 1
print('\n\033[32mCERTA RESPOSTA!!\033[m')
print('Você precisou de {} tentativas.'.format(tentativas))
