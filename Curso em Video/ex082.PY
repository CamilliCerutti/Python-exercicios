# DIVIDINDO VALORS EM VARIAS LISTAS
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.




valores = list()
impar = list()
par = list()
while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        par.append(num)
    elif num % 2 != 0:
        impar.append(num)
    valores.append(num)

    resp = input('Quer continuar? [S/N]: ').upper()
    if 'N' in resp:
        break

print(f'A lista completa é: {valores}\nOs valores pares são: {par}\nOs valores impares são: {impar}')