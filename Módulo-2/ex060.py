num = int(input('Digite um número para descobrir o seu fatorial: '))
fat = 1
print('{}! = {} X '.format(num, num), end='')
while num > 1:
    fat = fat * num
    num -= 1
    if num > 1:
        print('{} X '.format(num), end='')
    else:
        print('{} = {}'.format(num, fat))
