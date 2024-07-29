#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

'''cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** 0.5

print('A hipotenusa tem o comprimento {:.2f4}'.format(hipotenusa))'''

from math import hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipotenusa = hypot(cateto_adjacente, cateto_oposto)

print('A hipotenusa tem o comprimento {:.2f}'.format(hipotenusa))
