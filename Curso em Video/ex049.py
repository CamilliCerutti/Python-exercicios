# TABUADA v2.0
# Refaça o ex 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

x = int(input('Digite um número: '))

for a in range(1 ,10+1):
    resultado = x * a
    print(f'{x} x {a} = {resultado}')
