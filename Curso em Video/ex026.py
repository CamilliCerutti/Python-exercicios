#  PRIMEIRA E ULTIMA OCORRÊNCIA DE UMA STRING
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('digite uma frase: ')).strip().lower()
quant = frase.count('a')
show = frase.find('a')
shou = frase.rfind('a')

print(f'A letera "a" aparece {quant} vezes')
print(f' E aparece pela primeira vez na posição {show}')
print(f'E aparece pela ultima vez na posição {shou}')