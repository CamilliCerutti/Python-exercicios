# JOGO DE ADVINHAÇÃO V1.0
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

num = int(input('Pensei em um número entre 0 e 5. Tente advinhar qual é este número: '))

c = randint(0,5)

print('PROCESSANDO...')

sleep(3)

print(f'O numero que eu pensei foi {c}')

if num == c:
    print('Voce acertou, parabens!')
else:
    print('Voce errou, tente novamente!')
