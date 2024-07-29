tupla = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
impar = 0
print(f'O número 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece na {tupla.index(3) + 1}ª posição.')
else:
    print('O número 3 não aparece nos números selecionados.')
print('Os valores pares digitados foram ', end='')
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
    else:
        impar += 1
        if impar == 4:
            print('"nenhum".')