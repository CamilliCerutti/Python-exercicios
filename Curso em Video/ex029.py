# RADAR ELETRÔNICO
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    print(f'MULTADO! Você excedeu o limite que é de 80km/h e sua multa é no valor de: R${(vel-80) * 7:.2f}')
else:
    print('Continue dirigindo com cuidado')
print('Tenha um bom dia! dirija com segurança!')