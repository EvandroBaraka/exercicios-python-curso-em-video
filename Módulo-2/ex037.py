# Escreva um programa que leia um número inteiro qualquer a peça para o usuário escolher qual será a base de conversão: 
# 1 para binário 
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Digite a opção de converção desejada:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('O número {} em BINÁRIO fica: {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} em OCTAL fica: {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} em HEXADECIMAL fica: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
