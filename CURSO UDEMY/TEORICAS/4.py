while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('digite o operador: ')
    sair = input('Desejsa sair? [s/n]: ').lower()

    if sair in 'ssim':
        break

    if num_1.isdigit() and num_2.isdigit():
        num_1 = int(num_1)
        num_2 = int(num_2)

        if operador == '+':
            print(num_1 + num_2)

        elif operador == '-':
            print(num_1 - num_2)

        elif operador == '/':
            print(num_1 / num_2)

        elif operador == '*':
            print(num_1 * num_2)

        else:
            print('Digite um operador valido')

    else:
        print('Digite um numero valido!')
