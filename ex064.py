n = 0
t = 0
c = 0
while n != 999:
    n = int(input('Digite um número inteiro: '))
    if n != 999:
        t += n
        c += 1
print('Foram digitados {} números.'.format(c))
print('A soma de todos números digitados é {}'.format(t))