from time import sleep

print('{:=^50}'.format('OPERAÇÕES MATEMÁTICAS'))
opcao = 1
while opcao != 0:
    print('''Qual operação deseja realizar:
        [ 1 ] SOMA
        [ 2 ] SUBTRAÇÃO
        [ 3 ] MULTIPLICAÇÃO
        [ 4 ] DIVISÃO
        [ 5 ] MAIOR
        [ 0 ] SAIR''')
    opcao = int(input('Digite a opção: '))
    while opcao not in [0, 1, 2, 3, 4, 5]:
        print('Opção inválida')
        opcao = int(input('Digite novamente: '))
    if opcao != 0:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
        if opcao != 0:
            if opcao == 1:
                print('{} + {} = {}'.format(n1, n2, n1+n2))
            elif opcao == 2:
                print('{} - {} = {}'.format(n1, n2, n1-n2))
            elif opcao == 3:
                print('{} X {} = {}'.format(n1, n2, n1*n2))
            elif opcao == 4:
                print('{} / {} = {}'.format(n1, n2, n1/n2))
            elif opcao == 5:
                print('{} é o maior.'.format(n1) if n1 > n2 else '{} é o maior'.format(n2))
        print('\n') 
        sleep(2)
print('ENCERRANDO APLICAÇÃO')
sleep(2)
