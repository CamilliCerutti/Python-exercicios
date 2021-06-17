# AUMENTOS MULTIPLOS
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

val = float(input('Qual o valor do seu salario?: R$'))

quin = val + (val * 0.15)
dez = val + (val * 0.10)

if val > 1250:
    print(f'Houve um aumento de 10% no seu salario, agora ele sera no valor R${dez:.2f}')
else:
    print(f'Houve um aumento de 15% no seu salario, algora ele sera no valor de R${quin:.2f}')
