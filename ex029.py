#faça um programa que leia a velocidade de um carro. Se ele ultrapassou 80km/h ele será multado em R$7.00 para cada km exedente.

vel = int(input('Digite a velocidade do carro: '))

if vel > 80 :
    print('Você ultrapassou o limite em {}km/h. Você será multado em R$ {:.2f}'.format(vel - 80, (vel - 80) * 7))
else:
    print('Velocidade OK')
