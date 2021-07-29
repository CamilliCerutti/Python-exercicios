string = 'o brasil é o o o o  pais do futebol, o brasil é o penta'
lista_1 = string.split(' ')
lista_2 = string.split(',')

# print(lista_1)
# print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    # print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é a palavra {palavra}({contagem}x)')