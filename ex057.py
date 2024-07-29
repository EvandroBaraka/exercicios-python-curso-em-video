sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MF':
    print('Opção inválida.')
    sexo = str(input('Digite novamente [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))