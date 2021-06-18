# ANALISE DE DADOS EM UMA TUPLA
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))

print(f'Os valores digitados foram {tupla}')

print(f'O valor 9  aparece {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O primeiro valor 3 foi digitado na{tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for c in tupla:
    if tupla % 2 == 0:
        print(tupla, end='')
