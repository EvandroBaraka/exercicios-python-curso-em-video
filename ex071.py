print('=' * 40)
print('{:^40}'.format('BANCO PASSAIA'))
print('=' * 40)
valor_saque = int(input('Quanto deseja sacar? R$ '))
print('-' * 30)
nota = 50
quant_notas = 0

while True:
    if valor_saque >= nota:
        valor_saque -= nota
        quant_notas += 1
    else:
        if quant_notas > 0:
            print(f'Total de {quant_notas} notas de R${nota:.2f}')
        
        if nota == 50:
            nota = 20
            quant_notas = 0
        elif nota == 20:
            nota = 10
            quant_notas = 0
        elif nota == 10:
            nota = 5
            quant_notas = 0
        elif nota == 5:
            nota = 1
            quant_notas = 0
        else:
            break
