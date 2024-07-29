# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÂO
# Média 7.0 ou superior: APROVADO

print('\033[1;34m===' * 11)
print('PROGRAMA DE AVALIAÇÃO DE ALUNO.')
print('===' * 11)
print('\033[m')

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media < 5:
    print('\033[1;30;41m REPROVADO \033[m')
    print('Sua média foi {:.1f}. Você não atingiu a média necessária'.format(media))
elif media >= 5 and media < 7:
    print('\033[1;30;43m RECUPERAÇÃO \033[m')
    print('Sua média foi {:.1f}. Você deverá fazer a recuperação'.format(media))
elif media >= 7:
    print('\033[1;30;42m APROVADO \033[m')
    print('Parabéns! Sua média foi {}. Você foi aprovado.'.format(media))
