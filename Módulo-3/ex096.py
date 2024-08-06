def area(l, c):
	a = l * c
	print(f'A área de um terreno {l}x{c} é de {a}m²')
	

print('-' * 20)
print(f'{"CONTROLE DE TERRENO":^20}')
print('-' * 20)

larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))

area(larg, comp)
