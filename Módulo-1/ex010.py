# Crie um programa que leia quantos reais uma pessoa tem na carteira e diga quantos dólares ela pode comprar.
# Considere o valor do dolar em U$5,25

real = float(input('Quantos reais você tem? '))
dolar = float(5.25)

compra = real / dolar

print('Com R${:.2f} é possível comprar U${:.2f}'.format(real, compra))
