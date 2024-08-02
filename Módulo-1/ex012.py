#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valor = float(input('Digite o valor do produto: '))

novo_valor = valor - (valor * 0.05)

print('Na promoção com 5% de desconto o produto custará R${:.2f}'.format(novo_valor))
