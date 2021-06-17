# CALCULANDO A MÉDIA v2.0
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print(f'REPROVADO! Sua média foi: {m:.1f}.')
elif 5 <= m < 6.9:
    print(f'RECUPERAÇÃO! Sua média foi: {m:.1f}')
elif m > 7:
    print(f'APROVADO! Sua média foi:{m:.1f}')