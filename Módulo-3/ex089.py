todosAlunos = []

while True: 
    nome = str(input('Digite o nome do aluno: ')).upper().strip()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2) / 2
    todosAlunos.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if continuar in 'Nn':
        break
print('-=' * 20)
print(f'{"N°":<4} {"NOME":<10} {"MÉDIA":>5}')
for i, c in enumerate(todosAlunos):
    print(f'{i:<4} {c[0]:<10} {c[2]:>5.1f}')
print('-' * 30)
while True:
    opc = int(input('Digite o número do aluno que deseja ver as notas (999 encerra): '))
    if opc == 999:
        break
    else:
        print(f'O aluno {todosAlunos[opc][0]} tirou as notas {todosAlunos[opc][1]}')
        print('-' * 40)
