# CLASSIFICANDO ATLETAS
#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
ida = int(input('Qual o ano de nascimento do atleta? '))

m = date.today().year - ida

print(f'O atleta tem {m} anos')

if m <= 9:
    print('A sua categoria é: MIRIM')
elif m <= 14:
    print('Sua categoria é: INFANTIL')
elif m < 19:
    print('Sua categoria é: JUVENIL')
elif m <= 25:
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')