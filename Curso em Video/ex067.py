# TABUADA v3.0
# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um numero: '))
    print('=-' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        result = n * c
        print(f'{n} x {c} = {result}')
    print('=-' * 20)

print('Numero invalido. Finalizando o programa.')
