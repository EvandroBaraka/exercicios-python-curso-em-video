from random import randint
from time import sleep

print('-=' * 15)
print(f'{"GERADOR DE JOGOS MEGA-SENA":^30}')
print('-=' * 15)
num = int(input('Quantos jogos deseja gerar? '))
listaJogos = []
jogo = []

for r in range(0, num):
    for n in range(0, 6):
        gerado = randint(1, 60)
        jogo[n].append(int(randint(1, 60)))