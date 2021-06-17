# SORTEANDO UM ITEM NA LISTA
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3:')
a4 = input('Digite o nome do aluno 4: ')

lista = [a1, a2, a3, a4]

print(f'O aluno que ira apagar o quadro é o aluno: {random.choice(lista)}')
