soma = 0
cont = 0
while True:
    n = int(input('Digite um valor (999 para sair): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números, e a soma deles é {soma}')