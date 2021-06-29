# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"

nome = input('Digite seu nome: ')

letras = len(nome)

if letras <= 4:
    print('Seu nome é curto')

elif 5 <= letras <= 6:
    print('Seu nome é normal')

elif letras > 6:
    print('Seu nome é muito grande')