# ANALISADOR DE TEXTOS
# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu  nome completo: ')).strip()

print('Todas as letras maiusculas: ', nome.upper())
print('Todas as letras minusculas: ', nome.lower())
print('Seu nome ao todo tem : ',len(nome)-nome.count(' '),'letras')
X = nome.split()
print('Seu primeiro nome tem: ', len(X[0]),'letars')

