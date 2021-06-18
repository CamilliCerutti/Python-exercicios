# SOMA ÍMPARES MÚLTIPLOS DE TRÊS
# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
cont = 0

for a in range (1, 500, 2):
    if a % 3 == 0:
        cont += 1
        s += a
        
print(f'A soma é:{s}')
print('FIM')