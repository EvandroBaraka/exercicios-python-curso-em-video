# Faça um programa que leia o salário de um funcionário e diga quanto ele receberá de aumento
# Se ele ganha menos de R$1250.00, terá um aumento de 15%
# Se ele ganha mais terá um aumento de 10%

salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    salario = salario + salario * 0.10
    print('O funcionário terá um aumento de 10%, e seu novo salário será R${:.2f}'.format(salario))
else:
    salario = salario + salario * 0.15
    print('O funcionário terá um aumento de 15%, e seu novo salário será R${:.2f}'.format(salario))