# Faça um programa que leia a altura e a largura de uma parede em metros
# calcule a área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2

print('A parede tem uma área de {:.2f}m, e serão necessários {:.2f} litros de tinta.'.format(area, tinta))
