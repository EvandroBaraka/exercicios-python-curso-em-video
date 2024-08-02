#Faça um programa que leia três números e diga qual é o maior e qual é o menor

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

print('O MAIOR número é o {}'.format(max(n1, n2, n3)))
print('O MENOR número é o {}'.format(min(n1, n2, n3)))