# CALCULANDO DESCONTOS
# Faça um algoritmo que leia o preço de um produto  e mostre seu novo preço, com 5% de desconto.

x = float(input('Qual o valor do produto? '))
a = x-(x * 0.05)

print(f'O valor do produto com 5% de desconto é: R${a:.2f}')
