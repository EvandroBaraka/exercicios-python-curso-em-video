#Faça um programa qua mostra na tala uma contagem regressiva para o estouro de fogos de artificio. indo de 10 até 0. com uma pausa da 1 segundo entre eles.

from time import sleep

input('Pressione enter para iniciar a contagem regressiva.')
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('BOOOMMM!!!')