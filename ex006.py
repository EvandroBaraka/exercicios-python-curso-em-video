# Crie um programa q leia um número, depois mostre seu dobro, triplo e raiz quadrada

num = int(input('digite um número: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {}'.format(num, dobro, triplo, raiz))
