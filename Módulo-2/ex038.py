# escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem.
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('Digire o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O primeiro número é maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
else:
    print('O segundo número é o maior.')
