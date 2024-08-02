from operator import itemgetter
from random import randint
from time import sleep

dados = dict()
ranking = list()
print('Valores sorteados:')
for d in range(1, 5):
    num = int(randint(1,6))
    dados[f'Jogador {d}'] = num
    print(f'O jogador {d} tirou {num}')
    sleep(0.8)
print('-=' * 20)

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('  == RANKING DE JOGADORES ==')
for i, c in enumerate(ranking):
    print(f'  {i + 1}º lugar: {c[0]} com {c[1]}')
    
    