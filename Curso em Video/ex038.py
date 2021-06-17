#COMPARANDO NÚMEROS
# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))


if num > num2:
    print(f'O primeiro valor é o maior')
elif num < num2:
    print(f'O Segundo numero é o maior')
else:
    print(f'nao existe valor maior. Os dois numeros são iguais')