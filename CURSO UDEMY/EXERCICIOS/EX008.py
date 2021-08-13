"""
CRIE UMA FUNÇÃO QUE RECEBA 2 NÚMEROS. O PRIMEIRO É UM VALOR E O SEGUNDO UM PERCENTUAL. RETORNE O VALOR DO PRIMEIRO NUMERO SOMADO DO AUMENTO DO PERCENTUAL DO MESMO.
"""

n1 = int(input('Digite um numero: '))
porcentagem = int(input('Digite o percentual: ')) 

def soma(num = n1, porcento = porcentagem):
    valor_descontado = n1 * (porcentagem / 100)
    return n1 + valor_descontado

print(soma())