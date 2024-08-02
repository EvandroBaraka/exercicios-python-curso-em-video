#Desenvolva um programa que leia o primeiro termo a a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
print('Os 10 primeiros termos da PA são: ')
for c in range (t, r * 10 + t, r):
    print(c, end=' > ')
print('FIM')