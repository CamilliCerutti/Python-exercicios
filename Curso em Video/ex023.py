# SEPARANDO DÍGITOS DE UM NÚMERO
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

po = int(input('Digite um número entre 1 e 9999: '))

u = po // 1 % 10
d = po // 10 % 10
c = po // 100 % 10
m = po // 1000 % 10

print(f'sua unidade é: {u}')
print(f'sua dezena é: {d}')
print(f'Sua centena é: {c}')
print(f'Seu milhar é: {m}')