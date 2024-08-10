def leiaInt():
    while True:
        num = str(input('Digite um número inteiro: '))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[1;31mERRO. Digite um número inteiro válido.\033[m')
    return num


n = leiaInt()
print(f'Você digitou o número {n}')