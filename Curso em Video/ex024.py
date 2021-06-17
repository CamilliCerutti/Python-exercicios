# VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome da sua cidade:')).lower().strip()
print(cidade[:5] == 'santo')