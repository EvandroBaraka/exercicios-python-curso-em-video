def voto(a):
	from datetime import date
	
	idade = date.today().year - a
	condição = ''
	if idade < 18:
		condição = f'Com {idade} anos: NÃO VOTA'
	elif idade < 65:
		condição = f'Com {idade} anos: VOTO OBRIGATÓRIO'
	else:
		condição = f'Com {idade} anos: VOTO OPCIONAL'
	return condição


ano = int(input('Digite o ano de nascimento: '))

result = voto(ano)
print(result)