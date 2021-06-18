# JOGO DO PAR OU IMPAR
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint

vitoria = 0

while True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('O que você escolhe? [I/P]: ')).strip().upper()
    computador = randint(0, 10)
    resultado = jogador + computador
    total = jogador + computador
    if resultado % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    if escolha == 'P' and resultado == 'PAR':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU {resultado}')
        print('-' * 20)
        print('Você VENCEU')
        vitoria += 1
    elif escolha == 'I' and resultado == 'PAR':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU {resultado}')
        print('-' * 20)
        print('Você PERDEU')
        break

    elif escolha == 'I' and resultado == 'IMPAR':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU {resultado}')
        print('-' * 20)
        print('Você VENCEU')
        vitoria += 1
    elif escolha == 'P' and resultado == 'IMPAR':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU {resultado}')
        print('-' * 20)
        print('Você PERDEU')
        break

print(f'Game over, você venceu {vitoria} vezes')
