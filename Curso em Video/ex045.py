# GAME: PEDRA PAPEL E TESOURA
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

#CORES USADAS NO TERMINAL
am = '\033[1;33m'
rox = '\033[1;35m'
az = '\033[1;31m'
cin = '\033[1;36m'
ver = '\033[1;32m'
mel = '\033[1;31m'
clear = '\033[m'

print('=-' * 20)
print(f'Vamos jogar {az}PEDRA{clear}, {ver}PAPEl{clear} ou {cin}TESOURA{clear}!')
print('=-' * 20)
sleep(1)

pergunta = int(input(f'''Escolha uma opção para se jogar:
{az}[ 0 ] Pedra{clear}
{ver}[ 1 ] Papel{clear}
{cin}[ 2 ] Tesoura{clear}
Digite sua opção: '''))
lista = ['pedra', 'papel', 'tesoura']
computador = randint(0, 2)
print(' ')
print(f'{am}JÓ')
sleep(1)
print(f'{rox}KEN')
sleep(1)
print(f'{am}POOH{clear}')
print(' ')

print(f'''Você escolheu: {lista[pergunta]}
O computador escolheu: {lista[computador]}''')
if computador == pergunta:
    print(f'{am}EMPATE{clear}!')
elif computador == 0: # computador jogou pedra
    if pergunta == 1:
        print(f'Computador perdeu, {cin}você ganhou{clear}!')
    if pergunta == 2:
        print(f'{mel}Você perdeu{clear}, Computador ganhou!')
    else:
        print(f'{mel}Operação invalida!')
elif computador == 1: # computador jogou papel
    if pergunta == 2:
        print(f'Computador perdeu, {cin}Voce ganhou!')
    if pergunta == 0:
        print(f'{mel}Computador ganhou{clear}, Você perdeu!')
elif computador == 2: # computador jogou tesoura
    if pergunta == 1:
        print(f'{mel}Computador ganhou{clear}, Você perdeu!')
    if pergunta == 0:
        print(f'Computador perdeu, {cin}Voce ganhou!')
else:
    print(f'{mel}Operação invalida!')
