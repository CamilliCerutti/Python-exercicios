# CONTANDO VOGAIS EM TUPLA
# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


palavras = ('exceto', 'cinico', 'idoneo', 'ambito', 'nescio', 'merito')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')