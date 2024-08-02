maior = menor = cont = valor = 0
continuar = 'S'
while continuar == 'S':
    num = float(input('Digite o valor: '))
    valor += num
    if cont == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    cont += 1
    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Deseja continuar [S/N]: ')).strip().upper()[0]
print('Foram digitados {} valores, e a média deles é de {}.'.format(cont, valor / cont))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))
