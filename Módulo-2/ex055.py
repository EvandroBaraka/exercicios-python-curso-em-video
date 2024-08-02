#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
pessoa_maior = 0
pessoa_menor = 0

for c in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
        pessoa_maior = c
        pessoa_menor = c
    else:
        if peso > maior:
            maior = peso
            pessoa_maior = c
        if peso < menor:
            menor = peso
            pessoa_menor = c

print('O maior peso registrado foi {}kg da {} pessoa.'.format(maior, pessoa_maior))
print('E o menor peso registrado foi {}kg da {} pessoa.'.format(menor, pessoa_menor))
