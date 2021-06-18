# CRIANDO UM MENU DE OPÇÕES
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


num = int(input('Digite um número: '))
num2 = int(input('Digite o segundo numero: '))

maior = 0
opcao = 0

while opcao != 5:
    print('=-'*30)
    opcao = int(input('''Digite o que deve ser feito de acordo com o menu:

    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa

    Digite sua opção: '''))

    if opcao == 1:
        opcao += 1

        print(f'O resultado de {num} + {num2} é {num + num2}')

    elif opcao == 2:

        print(f'O resultado de {num} x {num2} é {num * num2}')
        opcao += 1

    elif opcao == 3:
        opcao += 1

        if num > num2:
            maior = num
        else:
            maior = num2

        print(f'O maior número entre {num} e {num2} é {maior}')
    elif opcao == 4:
        print('Digite os valores novamente: ')
        num = int(input('Digite um número: '))
        num2 = int(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opcão invalida!')

print('=-' * 30)
print('Fim do programa. volte sempre!')
