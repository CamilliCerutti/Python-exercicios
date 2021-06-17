# DISSECANDO UMA VARIÁVEL
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabetico?', x.isalpha())
print('É alfanumerico?', x.isalnum())
print('esta em maiuscula?', x.isupper())
print('Está em minuscula?', x.islower())
print('Esta capitalizada?', x.istitle())
