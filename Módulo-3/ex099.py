from time import sleep

def maior(* num):
    maior = 0
    print('-=' * 15)
    print('Analisando os valores passados...')
    if len(num) > 0:
        maior = max(num)
        for i in num:
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
        
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print()



maior(5, 9, 2, 8, 0, 9)
maior(2, 5, 3)
maior(6)
maior(7, 4)
maior()