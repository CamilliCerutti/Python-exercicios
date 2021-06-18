# ESTATISTICAS EM PRODUTOS
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

st = sm = maior = menor = nome = cont = 0

barato = ''

while True:
    nome = str(input('DIGITE O NOME DO PRODUTO: ')).strip()
    preco = float(input('DIGITE O PREÇO DO PRODUTO: R$'))
    cont += 1
    if cont == 1:
        maior = preco
        menor = preco
    else:
        if preco < menor:
            menor = preco
            barato = nome
    st += preco
    if preco >= 1000:
        sm += 1
    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()[0]
    if usuario in 'N':
        break
    
print('=-' * 20)
print(f'O total da compra foi R${st:.2f}')
print(f'Temos {sm:.2f} produtos custando mais de R$1000')
print(f'O produto mais barato custa R${menor:.2f} e é o {barato}')