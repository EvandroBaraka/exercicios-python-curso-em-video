#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('No ângulo {}º, o seno vale {:.2f}, o cosseno vale {:.2f} e a tangente vale {:.2f}'.format(angulo, seno, cosseno, tangente))
