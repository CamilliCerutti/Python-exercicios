# GERENCIADOR DE PAGAMENTOS
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto? '))
opcao = int(input('''Selecione qual vai ser a forma de pagamento:
[ 1 ]À vista no dinheiro/cheque (10% de desconto)
[ 2 ]À vista no cartão (5% de desconto)
[ 3 ]Até 2x no cartão
[ 4 ]3x ou mais(20% de juros)
'Digite a opção: '''))

x = (valor * 0.20)

if opcao == 1:
    print(f'O valor a ser pago é R${valor - (valor * 0.10):.2f}.')
elif opcao == 2:
    print(f'O valor a ser pago é R${valor - (valor * 0.05):.2f}.')
elif opcao == 3:
    print(f'O valor a ser pago é: R${valor:.2f}')
elif opcao == 4:
    parcela = int(input('Em quants parcelas?'))
    pc = (valor + x) / parcela
    print(f'Sua compra parcelada em {parcela}x de R${pc:.2f} COM JUROS. O valor total a ser pago é: R${valor + (valor * 0.20):.2f}.')
