# LISTA DE PREÇOS COM TUPLAS
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.


print('~' * 40)
titulo = 'LISTA DE PRECOS'
print(titulo.center(30, ' '))
print('~' * 40)

lista = ('arroz', 5.00, 'feijão', 2.50,  'óleo de cozinha', 1.50,  'farinha de trigo', 20.00, 'sal', 1.50, 'açúcar', 2.90, 'café', 2.00)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('~' * 40)