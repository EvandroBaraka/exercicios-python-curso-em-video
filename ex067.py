from time import sleep
print('{:=^40}'.format('TABUADAS'))
while True:
    num = int(input('Digite um número (Nº negativo encerra o programa): '))
    print('PROCESSANDO...')
    sleep(1)
    print('=' * 40)
    if num < 0:
        break
    else:
        for c in range (1, 11, 1):
            print(f'{num} x {c} = {num * c}')
print('ENCERRANDO O PROGRAMA...')
sleep(2)
print('Finalizado. Até a proxima!!')
