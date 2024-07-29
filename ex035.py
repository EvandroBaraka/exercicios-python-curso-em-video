#desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo
print('-=-' * 20)
print('PROGRAMA PARA CALCULAR A EXISTENCIA DE TRIÂNGULO')
print('-=-' * 20 + '\n')

a = float(input('Digite o tamanho do primeiro lado: '))
b = float(input('Digite o tamanho do segundo lado: '))
c = float(input('Digite o tamanho do terceiro lado: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('Estes três lados formam um triângulo.')
else:
    print('Estes três lados NÃO formam um triângulo.')
