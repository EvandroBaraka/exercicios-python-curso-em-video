# Faça um programa que leia uma frase pelo teclado e diga:
# Quantas vezes aparece a letra 'a' 
# Em que posição ela aparece pela primeira vez 
# Em que posição ela aparece pela ultima vez

frase = input('Digite uma frase: ')
print('A letra -a- aparece {} vezes na sua frase.'.format(frase.count('a')))
print('Ela aparece pela primeira vez na posição {}'.format(frase.find('a') + 1))
print('Ela aparece pela ultima vez na posição {}'.format(frase.rfind('a') + 1))