# Elabore um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal a condição de pagamento:
# - à vista dinheiro/ cheque: 10% da desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: praso normal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o valor do produto: R$'))
opcao = int(input('''Digite o número correspondente a opção de pagamento desejada:
    [1] à vista dinheiro/cheque
    [2] à vista no cartão
    [3] até 2x no cartão
    [4] 3x ou mais no cartão
    Digite a opção escolhida: '''))
if opcao == 1 :
    print('O valor final será R${:.2f} já com 10% de desconto'.format(preco - (preco * 0.10)))
elif opcao == 2:
    print('O valor final será R${:.2f} já com 5% de desconto'.format(preco - (preco * 0.05)))
elif opcao == 3 :
    print('O valor final será R${:.2f}, sem desconto'.format(preco))
elif opcao == 4 :
    print('O valor final será R${:.2f} já com acréssimo de 20% de juros.'.format(preco + (preco * 0.20)))
    