# CONVERSOR DE MEDIDAS
# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

x = float(input('Digite uma distancia em metros: '))

cm = x * 100
mm = x * 1000
km = x / 1000
dam = x /10
hc= x / 100

print(f'{cm}cm\n{mm}mm\n{dam}dam\n{hc}hc\n{km}km')

