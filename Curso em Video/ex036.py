# APROVANDO EMPRÉSTIMO
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))

ao = 12
mes = ano * 12
vp = casa / mes
vss = 0.30 * salario

print(f'Para pagar uma cada de R${casa:.2f} em {ano} anos o valor da prestaçãp sera R${vp:.2f}')
if vp > vss:
    print('Emprestimo NEGADO')
elif vp <= vss:
    print('O emprestimo pode ser CONCEDIDO!!')
