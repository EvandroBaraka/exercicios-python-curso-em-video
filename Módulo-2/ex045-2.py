# escreva um programa que faça o computador jogar jokempo com o usuário

from random import randint
from time import sleep

print('{:=^40}'.format(' JOKENPO '))

continuar = 's'
while continuar == 's' :
    jokenpo = ('PEDRA', 'PAPEL', 'TESOURA')
    comp = randint(0, 2)
    jog = int(input('''Suas opções: 
[ 1 ] PEDRA
[ 2 ] PAPEL 
[ 3 ] TESOURA 
Qual você escolhe? ''')) - 1

    while jog != 0 and jog != 1 and jog != 2:
            print('Opção inválida')
            jog = int(input('Digite novamente: '))
    
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!')
    sleep(0.2)
    print('-=-' * 10)
    print('O jogador escolheu {}'.format(jokenpo[jog]))
    print('O computador escolheu {}'.format(jokenpo[comp]))
    print('-=-' * 10)
        
    if comp == 0 and jog == 0 or comp == 1 and jog == 1 or comp == 2 and jog == 2:
        print('\033[32mEMPATE\033[m')
    elif comp == 0 and jog == 2 or comp == 1 and jog == 0 or comp == 2 and jog == 1:
        print('\033[31mO computador ganhou!!\033[m')
    else:
        print('\033[34mO jogador ganhou!!\033[m')
    continuar = str(input('Deseja jogar novamente (s/n): '))
    while continuar != 's' and continuar != 'n':
        print('Opção inválida')
        continuar = str(input('Digite novamente (s/n): '))
