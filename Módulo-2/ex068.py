from random import randint
print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0
while True:
    print('-=-' * 20)
    num_user = int(input('Escolha seu número: '))
    opcao_user = str(input('Você escolhe par ou ímpar [P/I]: ')).strip().upper()[0]
    while opcao_user not in 'PI':
        print('Opção inválida')
        opcao_user = str(input('Você escolhe par ou ímpar [P/I]: ')).strip().upper()[0]
    num_pc = randint(1, 10)
    soma = num_user + num_pc
    print('-' * 40)
    print(f'Você jogou {num_user} e o computador jogou {num_pc}. Total de {soma} ', end='')
    if soma % 2 == 0:
        print('DEU PAR')
        print('-' * 40)
        if opcao_user == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print('DEU ÍMPAR')
        print('-' * 40)
        if opcao_user == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
if vitorias == 0:
    print('GAME OVER. Você não venceu nenhuma vez.')
elif vitorias == 1:
    print(f'GAME OVER. Você venceu {vitorias} vez.')
else:
    print(f'GAME OVER. Você venceu {vitorias} vezes.')