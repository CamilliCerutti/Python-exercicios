# ANALISADOR COMPLETO
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homemaior = 0
nomehome = ''
mulher = 0
soma = 0

for c in range(1, 5):
    print(f'-----{c}ª PESSOA ------')
    nome = str(input(f'Nome: ')).strip().lower()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip().lower()
    soma += idade
    media = soma / 4
    if c == 1 and sexo == 'm':
        homemaior = idade
        nomehome = nome
    if sexo == 'm':
        homemaior = idade
        nomehome = nome
 
    if sexo == 'f' and idade < 20:
        mulher += 1

print(f'A media da idade do grupo é {media}.')
print(f'O homem mais velho tem {homemaior} anos e se chama {nomehome}.')
print(f'Tem {mulher} Mulheres com menos de 20 anos')
