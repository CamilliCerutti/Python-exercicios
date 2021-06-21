# EXTRAINDO DADOS DE UMA LISTA
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

num = list()
cont = ''
while True:
    valores = num.append(int(input('Digite um número: ')))
    cont = input('Quer continuar? [S/N]').upper()
    if cont == 'N':
        break
num.sort(reverse=True)

if 5 in num:
    print('O valor 5 esta na lista!')
else:
    print('O valor 5 nao esta na lista!')
print(f'A lista ordenada de forma decrescente é: {num}\nVoce digitou {len(num)} valores')