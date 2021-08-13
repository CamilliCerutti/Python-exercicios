"""
CRIE UMA FUNÇAO QUE EXIBE UMA SAUDAÇÃO COM OS PARAMETROS SAUDACAO E NOME
"""
nome1 = input('Digite seu nome: ')
def saudacao(msg = 'Ola', nome = nome1):
    print(msg, nome)

saudacao()