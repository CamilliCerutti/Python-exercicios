# PAR OU ÍMPAR?
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('digite um numero:'))

pr = num % 2

if pr == 0:
    print(f'o numero {num} é par')
else:
    print(f'O numero {num} é impar')