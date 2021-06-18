# TRATANDO VÁRIOS VALORES v1.0
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
s = 0

valor = int(input('Digite um numero'))

while valor != 999:
    s += valor
    valor = int(input('Digite um numero'))
    cont += 1

print(f'{cont} - {s}')
