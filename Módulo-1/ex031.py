#Desenvolva um programa que pergunta a distância de uma viagem em Km. Calcula o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km a R$0.45 para viagens mais longas.

distancia = float(input('Qual a distância da viagem em KM: '))

if distancia <= 200:
    print('Sua passagem custará R$ 0.50 por KM, com um total de R$ {:.2f}'.format(distancia * 0.50))
else:
    print('Como sua viagem tem mais de 200km sua passagem custará R$0.45 por km, com um total de R${:.2f}'.format(distancia * 0.45))