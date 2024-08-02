# Faça um programa que leia um número de 0 a 9999, e mostre na tela cada um dos digitos separadamente. 
# Exemplo: Número 1983 
# unidade: 3 
# dezena: 8 
# centena: 9 
# milhar: 1

num = int(input('Digite um número entre 0 e 9999: '))
m = num // 1000
c = num // 100 % 10
d = num // 10 % 10
u = num % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))