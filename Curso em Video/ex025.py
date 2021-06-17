# PROCURANDO UMA STRING DENTRO DE OUTRA
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Tem "silva", no seu nome? Digite seu nome completo: ')).strip()

print('silva' in nome.lower())