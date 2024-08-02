valores = []
for c in range(0, 5):
	num = int(input('Digite um número: '))
	if c == 0 or num >= valores[-1]:
		valores.append(num)
		print('Valor adicionado ao final da lista...')
	else:
		cont = 0
		while cont < len(valores):
			if valores[cont] >= num:
				valores.insert(cont, num)
				print(f'Valor adicionado a posição {cont} da lista...')
				break
			cont += 1
print(valores)