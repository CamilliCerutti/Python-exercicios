# JOGO DA ADVINHAÇÃO v2.0
# Melhore o jogo do ex 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

c = randint(0, 10)
percas = 0
while num != c:
    num = int(input('Voce errou! Digite outro número: '))
    percas += 1

print(f'O numero que eu pensei foi {c}. Você acertou mas precisou de {percas+1} tentativas.')

