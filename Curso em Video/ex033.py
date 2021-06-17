# MAIOR E MENOR VALORES
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um numero:'))
b = int(input('Digite outro numero:'))
c = int(input('Digite outro numero:'))

# Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    mior = c
    
print(f'O menor valor digitado é: {menor}')
print(f'O maior valor digitado é o {maior}')
