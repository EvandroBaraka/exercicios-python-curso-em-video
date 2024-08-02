# Cria um programa qua leia uma frase qualquer a diga sa ela é um palindromo. Desconsiderando os espaços.
# Ex:
# APOS A SOPA 
# A SACADA DA CASA 
# A TORRE DA DERROTA 
# O LOBO AMA O BOLO 
# ANOTARAM A DATA DA MARATONA

frase = str(input('Digite uma frase: ')).lower().split()
frase = ''.join(frase)

if frase == frase[::-1]:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

