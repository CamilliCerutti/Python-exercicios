# ALUGUEL DE CARROS
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quant = float(input('Quantos km você percorreu? '))
dias = int(input('Você alugou o carro por quantos dias? '))
preco = 60 * dias
precokm = 0.15 * quant
total = preco + precokm

print(f'Você alugou o carro por {dias} dias e percorreu {quant}Km\nO valor da diaria é: R$60,oo e é cobrado uma taxa de R$0,15 a cada km percorrido.\nSendo assim, O valor total a ser pago é de: R${total:.2f}.')
