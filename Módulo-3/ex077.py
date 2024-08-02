palavras = ('APRENDER', 'BRINCAR', 'JOGAR', 
			'PULAR', 'TELIVISÃO', 'LIQUIDIFICADOR', 
			'PYTHON', 'CURSO', 'ESTUDAR', 'AULA')

for c in palavras:
    print(f'A palavra {c} tem as vogais ', end='')
    '''for letras in range (0, len(c)):
        if c[letras] == 'A' or c[letras] == 'Ã':
            print('A', end=' ')
        if c[letras] == 'E':
            print('E', end=' ')
        if c[letras] == 'I':
            print('I', end=' ')
        if c[letras] == 'O':
            print('O', end=' ')
        if c[letras] == 'U':
            print('U', end=' ')
    print('\n')'''
    for letras in c:
    	if letras in 'AÃÂÁEÉÊIÍOÓÔÕUÚ':
    		print(letras, end=' ')
    print('\n')