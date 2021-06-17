# PINTANDO A PAREDE
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

x = float(input('Qual a largura da parede em metros? '))
y = float(input('Qual a altura da parede em metros? '))

a = x*y
um = 2
lt = a/2

print(f'Sua area é de: {a}m².\nPara pintar essa parede, voce vai precisar de:{lt:.3f}l de tinta.')