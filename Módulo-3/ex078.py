num = []
maiores = []
menores = []
for c in range (0, 5):
    num.append(int(input('Digite um número: ')))
for i, n in enumerate(num):
    if n == max(num):
        maiores.append(i)
    if n == min(num):
        menores.append(i)
print(f'Os valores digitados foram {num}')
print(f'{max(num)} é o maior número, encontrado nas posições {maiores}')
print(f'{min(num)} é o menor número, encontrado nas posições {menores}')