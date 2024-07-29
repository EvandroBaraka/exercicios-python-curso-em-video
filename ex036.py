# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo sera negado.

print('\033[1;33m===' * 20)
print('PROGRAMA PARA APROVAÇÃO DE FINANCIAMENTO DE CASA')
print('===' * 20 + '\033[m')

valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
meses = int(input('Em quantos anos será feito o pagamento: ')) * 12

prestacao = valor_casa / meses

if prestacao > (salario * 0.30):
    print('\033[1;31mFINANCIAMENTO NEGADO!!\033[m')
    print('O valor da parcela ficaria R${:.2f} que ultrapassa 30% do salário do comprador.'.format(prestacao))
else:
    print('\033[1;34;42mFINANCIAMENTO APROVADO!!\033[m')
    print('Serão {} parcelas de R${:.2f}.'.format(meses, prestacao))