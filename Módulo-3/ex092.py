from datetime import date

anoAtual = date.today().year
pessoa = {'Nome': str(input('Nome: ')), 
'idade': anoAtual - int(input('Data de nascimento: ')), 'CTPS': int(input('Número da CTPS (0 não tem): '))
}
if pessoa['CTPS'] != 0:
	pessoa['contratação'] = int(input('Data da contratação: '))
	pessoa['salário'] = float(input('Salário: '))
	pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - (anoAtual - pessoa['idade'])

for k, v in pessoa.items():
	print(f'{k} tem o valor {v}')