# Faça um programa que pergunte a hora ao usuario e, baseando-se no horario descrito, exiba a saudacao apropriada. 
# EX: bom dia 0-11, boa tarde 12-17 e boa noite 18-23

hora = input('Digite a hora: (0-23) ')

if hora.isdigit():
    hora = int(hora)

    if 0 <= hora <= 11:
        print('bom dia!') 
    
    elif 12 <= hora <= 17:
        print('Boa tarde!')
    
    elif 18 <= hora <= 23:
        print('Boa noite!')

else:
    print('Por favor, digite um horario entre 0 e 23.')
