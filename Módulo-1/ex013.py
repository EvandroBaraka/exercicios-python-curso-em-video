# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o salário atual do funcionário: R$'))
novo_salario = salario + (salario * 0.15)

print('O salário com 15% de aumento fica R${:.2f}'.format(novo_salario))
