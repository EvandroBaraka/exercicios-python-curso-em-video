# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- Equilátero: todos os lados iguais
#- Isósceles: dois lados iguais
#- Escelano: todos os lados diferentes

a = float(input('Digite o tamanho do primeiro lado: '))
b = float(input('Digite o tamanho do segundo lado: '))
c = float(input('Digite o tamanho do terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Estes três lados podem formar um triângulo Equilátero.')
    elif a == b != c or a == c != b or b == c != a:
        print('Estes três lados podem formar um triângulo Isóceles.')
    else:
        print('Estes três lados podem formar um triângulo Escaleno.')
else:
    print('Estes três lados NÃO podem formar um triângulo.')