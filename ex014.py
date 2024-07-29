# crie um algoritmo que leia graus C° e converta para F°. Fórmula: (F = C x 1.8 + 32)

c = float(input('Digite a temperatura em Celsius para converter para Farenheit: '))
f = c * 1.8 + 32
k = c + 273.15

print('A temperatura de {:.1f}C° é equivalente a {:.1f}F° ou {:.1f}K°.'.format(c,  f, k))