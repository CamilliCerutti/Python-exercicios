# CONVERSOR DE BASES NUMÉRICAS
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num =  int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para converter para BINARIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL''')

opcao = int(input('Digite sua opção: '))

if opcao == 1:
    print(f'Sua opção foi BINARIO. E o resultado é: {bin(num)}')
elif opcao == 2:
    print(f'Sua opção foi OCTAL. E o resultado é: {oct(num)}')
elif opcao == 3:
    print(f'Sua opção foi HEXADECIMAL. E o resultado é: {hex(num)}')