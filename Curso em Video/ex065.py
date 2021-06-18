# MAIOR E MENOR VALORES 
# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = cont = maior = menor = media = 0
continuidade = 'S'

while continuidade  in 'S':
    num = float(input('Digite um numero: '))
    soma += num
    cont += 1
    continuidade = str(input('Você quer continuar digitando valores, [S/N]: ')).strip().upper()
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    media = soma / cont

print(f'voce digitou {cont} números e a media foi {media:.2f}')
print(f'O maior valor é {maior} e o menor é {menor}')
