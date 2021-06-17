# ANALISANDO TRIÃNGULOS v2.0
# Refaça o EX 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < + a + c and c < a + b:
    print(f'Os segmentos acima podem formar um triangulo ', end= '')
    if a == b == c:
        print('Equilatero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('isoceles')
else:
    print('Os segmentos acima não podem formar um triangulo! ')