print('{:=^60}'.format('SEQUENCIA FIBONACCI'))
n = int(input('Digite quantos termos da sequencia de Fibonacci quer ver: '))
f1 = 0
f2 = 1
while n > 0:
    print('{} > '.format(f1), end='')
    t = f1 + f2
    f1 = f2
    f2 = t
    n -= 1
print('FIM')