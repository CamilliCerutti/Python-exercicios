# VALIDAÇÃO DE DADOS
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo: [M/F] ')).strip().lower()

while sexo not in 'mf':
    sexo = str(input('Dados invalidos. Informe o sexo: ')).strip().lower()
    
print(f'sexo {sexo} registrado com sucesso!')
print('Fim')
