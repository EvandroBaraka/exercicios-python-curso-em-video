#Faça um programa que calcule a soma entre todos os números impares que São múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Soma dos números ímpares multiplos de 3, de 1 a 500')
soma = 0
for c in range (1, 501):
    if (c % 2) == 1:
        if (c % 3) == 0:
            #soma = soma + c
            soma += c
print('A soma dos multiplos de 3 até 500 é {}'.format(soma))
        