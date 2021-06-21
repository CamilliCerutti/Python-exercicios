# VALORES UNICOS EM UMA LISTA
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 


num = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)

    resposta = input('Quer continuar? [S/N] ').upper()
    if resposta in 'N':
        break
num.sort()
print(num)
