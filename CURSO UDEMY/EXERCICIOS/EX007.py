"""
CRIE UMA FUNÇÃO QUE RECEBA 3 NÚMEROS COMO PARAMETROS E EXIBA A SOMA ENTRE ELES.
"""
from random import randint

def soma(x = randint(0,9), y = randint(0,9), z = randint(0,9)):
    print(f'os numeros escolhidos foram {x, y, z} e a soma entre eles é: {(x + y)+ z}')

soma()