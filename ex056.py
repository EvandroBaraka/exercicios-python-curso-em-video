#Desenvolva um programa que leia o nome, idade a sexo da 4 pessoas. No final do programa, mostre:
#A média de idade do grupo.
#Qual é o nome do homem mais velho. #Quantas mulheres têm menos de 20 anos.

nome_homem = ''
idade_homem = 0
media_idade = 0
mulheres20 = 0

for c in range (1, 5):
    print('---- {}ª Pessoa ----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Opção inválida. Digite novamente (M/F): ')).upper()
    media_idade += idade
    if sexo == 'F' and idade < 20:
        mulheres20 += 1
    if sexo == 'M':
        if idade_homem < idade:
            nome_homem = nome
            idade_homem = idade

print('A média de idade do grupo é de {:.1f} anos.'.format(media_idade / 4))
print('O homem mais velho é o {} que tem {} anos.'.format(nome_homem, idade_homem))
print('Foram informadas {} mulheres com menos de 20 anos.'.format(mulheres20))
    