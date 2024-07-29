#Crie um programa que leia um número do usuário e diga se ele é PAR ou IMPAR

print('PROGRAMA PARA DESCOBRIR SE O NÚMERO É PAR OU IMPAR')
continuar = 'S'

while continuar == 'S':
    num = int(input('\nDigite o número: '))
    if num % 2 != 0 :
        print('{} é IMPAR'.format(num))
    else:
        print('{} é PAR'.format(num))
    pergunta = input('Deseja tentar outro número (S/N): ').strip().upper()
    continuar = pergunta[0]