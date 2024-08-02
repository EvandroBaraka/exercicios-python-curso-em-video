from random import randint
from time import sleep

listaJogos = []
jogo = []

print('-=' * 15)
print(f'{"GERADOR DE JOGOS MEGA-SENA":^30}')
print('-=' * 15)
num = int(input('Quantos jogos deseja gerar? '))
print()
print(f'{" SORTEANDO JOGOS ":*^30}')
print()
for r in range(0, num):
    for n in range(0, 6):
        while True:
            numGerado = randint(1, 60)
            if numGerado not in jogo:
                jogo.append(numGerado)
                break
    listaJogos.append(jogo[:])
    listaJogos[r].sort()
    jogo.clear()
    sleep(1)
    print(f'Jogo {r + 1}: {listaJogos[r]}')
print()
print(f'{" BOA SORTE! ":=^30}')
