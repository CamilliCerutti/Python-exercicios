# SENO, COSSENO E TANGENTE
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = int(input('Digite um algulo: '))

print(f'O valor do cosseno é:{math.cos(math.radians(ang)):.2f}\nO valor do seno: {math.sin(math.radians(ang)):.2f}\nO valor da tangente é:{math.tan(math.radians(ang)):.2f}')