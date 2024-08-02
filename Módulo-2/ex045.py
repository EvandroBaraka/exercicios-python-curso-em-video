# escreva um programa que faça o computador jogar jokempo com o usuário

from random import choice

continuar = 's'
while continuar == 's' :
        jokenpo = ['pedra', 'papel', 'tesoura']
        jog = str(input('Você escolhe pedra, papel ou tesoura? ')).strip().lower()
        comp = choice(jokenpo)

        while jog != 'pedra' and jog != 'papel' and jog != 'tesoura':
                print(jog)
                print('Opção inválida')
                jog = str(input('Digite novamente: ')).strip().lower()
        
        print('O computador escolheu {}'.format(comp))
        
        if comp == 'pedra' and jog == 'pedra' or comp == 'papel' and jog == 'papel' or comp == 'tesoura' and jog == 'tesoura':
                print('Empate')
        elif comp == 'pedra' and jog == 'tesoura' or comp == 'papel' and jog == 'pedra' or comp == 'tesoura' and jog == 'papel':
                print('O computador ganhou!!')
        else:
                print('Você ganhou!!')
        continuar = str(input('Deseja jogar novamente (s/n): '))
        while continuar != 's' and continuar != 'n':
                print('Opção inválida')
                continuar = str(input('Digite novamente (s/n): '))
