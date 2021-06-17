#CONVESOR DE MOEDAS
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

x = float(input('Quanto de dinheiro você tem?: R$'))

u = 5.78 # Valor do dolar no dia que foi feito o exercício
s = x/u

print(f'De acordo com o valor que você tem na carteira, poderas comprar: US{s:.2f}')

