""" Criar variaveis para nome, idade, altura e ano atual
obter o ano de nascimento da pessoa(Baseado na idade e no ano atual
obter o imc da pessoa com 2 casas decimais
exibir um texto com todos os valores na tela usando f- strings)"""

nome = 'luiz'
idade = 34
peso = 80
altura = 1.80
ano = 2021
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}KG\nO IMC de {nome} é {imc:.2f}\n{nome} Nasceu em {ano -  idade}')