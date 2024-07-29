# Escreva um programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.
print('Calcular valor do aluguel do carro')
print('=' * 40)
dias = int(input('Digite o número de dias que ficou com o carro: '))
km = float(input('Digite o número de Km rodados: '))

total_dias = dias * 60
total_km = km * 0.15

print('\nVocê deverá pagar R${:.2f}\nSendo R${:.2f} referente aos dias, e R${:.2f} referente aos KM.'.format(total_dias+total_km, total_dias, total_km))
