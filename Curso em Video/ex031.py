# CUSTO DA VIAGEM
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distancia do trajedo da viagem?: '))
cinq = 0.50
C = 0.45

if dist <= 200:
    print(f'O valor a ser pago é: R${(cinq) * dist:.2f}')
else:
    print(f'O valor a ser pago é: R${C * dist:.2f}')
