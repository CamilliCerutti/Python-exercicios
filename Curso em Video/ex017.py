# CATETOS E HIPOTENUSAS
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, pow, hypot
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjascente: '))

hip = hypot(co, ca)

print(f'O valor da hipotenusa é: {hip:.2f}')