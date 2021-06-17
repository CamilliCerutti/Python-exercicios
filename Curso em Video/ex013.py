# REAJUSTE SALÁRIAL 
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

x = float(input('Qual é o salario do funcionario? R$'))
a = x+(x*0.15)

print(f'Você acaba de ganhar um aumento de 15%,\n entao seu salario ao inves de ser R${x:.2f} passou a ser R${a:.2f}')
