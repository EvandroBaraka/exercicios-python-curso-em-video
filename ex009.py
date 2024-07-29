#faça um programa que leia um numero inteiro e mostre a sua tabuada.

n1 = int(input('Digite um número inteiro: '))
tabuada = 1

while tabuada <= 10:
    print('{} X {} = {}'.format(n1, tabuada, n1*tabuada))
    tabuada += 1
