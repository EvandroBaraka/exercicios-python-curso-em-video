lista_produtos = ('Playstation 5', 3499, 'Joystick Dualsense', 349,
                  'Jogo God of War', 299, 'Cabo USB-C', 32.9, 
                  'Fone Pulse 3D', 449.59, 'Televisão Sony 60"', 3499,
                  'Livro', 19.65, 'Cadeira Gamer', 779.5)

print('-' * 50)
print('{:^50}'.format('LISTA DE PREÇOS'))
print('-' * 50)

for c in range (0, len(lista_produtos), 2):
    print(f'{lista_produtos[c]:.<40}R$ {lista_produtos[c + 1]:>7.2f}')
print('-' * 50)