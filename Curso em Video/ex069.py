# ANALISE DE DADOS DO GRUPO
# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

som = 0 #soma dos homens cadastrados
soo = 0 # soma das mulheres com menos de 20 anos

maioridade = 0

while True:

    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        sexo = 'Masculino'
        som += 1
    elif sexo == 'F' and idade < 20:
        sexo = 'Feminino'
        soo += 1
    usuario = ' '
    while usuario not in 'SN':
        usuario = str(input('Quer continuar?'))[0]
    if usuario in 'n':
        break
    
print(f'Foi cadastrado {soo} mulheres com menos de 20 anos.\n{som} Homens\nE {maioridade} Pessoas com mais de 18 anos.')