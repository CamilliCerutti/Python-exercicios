# NÚMEROS PRIMOS
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero inteiro: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
    
print(f'\n\033[mo numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E pos isso ele não é primo')
