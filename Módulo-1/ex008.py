# Escreva um programa que leia um valor em metros, e o exiba convertido em centimetros e milimetros.

metro = float(input('Digite o valor em metros: '))

centimetro = int(metro * 100)
milimetro = int(metro * 1000)

print('{} metros é o mesmo que {} centimetros e {} milimetros'.format(metro, centimetro, milimetro))