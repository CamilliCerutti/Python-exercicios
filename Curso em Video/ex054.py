# GRUPO DA MAIORIDADE
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input(f'Digite o{c}º ano de nascimento: '))
    idade = date.today().year - ano
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maior de idade\nE {menor} pessoas menor de idade.')
