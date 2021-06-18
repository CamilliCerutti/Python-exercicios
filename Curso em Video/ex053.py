# DETECTOR DE PALINDROMO
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. 

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
print(junto, inverso)
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('nao temos um palindromo!')

