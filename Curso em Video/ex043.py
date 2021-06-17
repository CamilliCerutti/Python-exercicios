# ÍNDICE DE MASSA CORPORAL
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / altura**2

if imc < 18.5:
    print(f'Seu IMC é: {imc:.2f}. Você está abaixo do peso!')
elif 18.5 < imc < 25:
    print(f'Seu IMC é: {imc:.2f}. Você está no peso ideal!')
elif 25 < imc < 30:
    print(f'Seu IMC é: {imc:.2f}. Você está com sobrepeso!')
elif 30 < imc < 40:
    print(f'Seu IMC é: {imc:.2f}. Você está com obesidade!')
elif imc > 40:
    print(f'Seu IMC é: {imc:.2f}. Você esta com obesidade morbida!')

