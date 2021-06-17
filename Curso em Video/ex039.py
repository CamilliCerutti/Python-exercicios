# ALISTAMENTO MILITAR
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Em que ano você nasceu? '))

dt = date.today().year - ano
falta = 18 - dt
resta = dt - 18
atual = date.today().year

print(f'Quem nasceu em {ano} tem {dt} anos em {date.today().year}')

if (date.today().year - ano) < 18:
    print(f' Ainda faltam {falta} anos para o alistamento.')
    print(f'Seu alistamento sera em {atual + falta}')

elif (date.today().year - ano) > 18:
    print(f'Você deveria ter se alistado há {resta}')
    print(f'Seu alistamento foi em {atual - falta}')

elif (date.today().year - ano) == 18:
    print('Esta na hora de voce se alistar!')
