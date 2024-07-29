expressao = str(input('Digite uma expressão: '))
lista = expressao[::]
cont = 0
for i in range(0, len(lista)):
	if lista[i] == '(':
		cont += 1
	elif lista[i] == ')':
		cont -=1
	if cont < 0:
		break
if cont == 0:
	print('Expressão válida...')
else:
	print('Expressão inválida...')
	