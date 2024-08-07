from random import randint
from time import sleep

def sortear(lista):
	for c in range(0, 5):
		num = randint(1, 10)
		lista.append(num)
def somaPar(lista, tot):
	tot = 0
	for c in lista:
		if c % 2 == 0:
			tot += c
	return tot

numeros = []
soma = 0

sortear(numeros)
soma = somaPar(numeros, soma)
print('Sorteando 5 valores da lista: ', end='', flush=True)
sleep(1)
for c in numeros:
	print(c, end=' ', flush=True)
	sleep(0.5)
print('PRONTO!')
sleep(0.5)
print(f'Somando os valores pares de {numeros} temos o total {soma}')
