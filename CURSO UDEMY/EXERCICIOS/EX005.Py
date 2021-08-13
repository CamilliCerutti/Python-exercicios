"""
DESAFIO: VALIDE UM CPF
"""

# Verificando o primeiro digito
while True:
    cpf = input('digite seu cpf: ')

    novo_cpf = cpf[:-2]

    reverso_1 = 10

    reverso_2 = 11

    resultado_1 = 0

    resultado_2 = 0

    for index_1 in range(9):

        total_1 = int(novo_cpf[index_1]) * reverso_1
        resultado_1 += total_1
        reverso_1 -= 1

        conta_1 = 11 - (resultado_1 % 11)

        if conta_1 > 9:
            digito_1 = 0

        else:
            digito_1 = conta_1 

    # VERIFICANDO O SEGUNDO DIGITO

    cpf_2 = novo_cpf + str(digito_1)

    for x in range(10):

        total_2 = int(cpf_2[x]) * reverso_2
        resultado_2 += total_2
        reverso_2 -= 1
        conta_2 = 11 - (resultado_2 % 11)
        
        if conta_2 > 9:
            digito_2 = 0
        else:
            digito_2 = conta_2

    cpf_novo = novo_cpf + str(digito_1) + str(digito_2)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf_novo == cpf and not sequencia:
        print('CPF VÁLIDO!')
        
    else:
        print('CPF INVÁLIDO!')
        
