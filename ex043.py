# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, e calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

print('\033[1;33m--*--' * 4)
print('CALCULADORA DE IMC')
print('--*--' * 4)
print('\033[m')

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))
imc = peso / (altura * altura)

print('Seu IMC é {}'.format(int(imc)))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Parabéns, você está no peso ideal.')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso.')
elif imc > 30 and imc <= 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')
