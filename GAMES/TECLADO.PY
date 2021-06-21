# jOGO DE TENTAR ESCREVER PALAVRAS NO TEMPO MAIS CURTO POSSIVEL

import requests
import random
import time

url ='http://www.mit.edu/~ecprice/wordlist.10000'

resposta = requests.get(url)
palavras = resposta.content.splitlines()

palavras = [ palavra.decode('utf-8')for palavra in palavras]

palavras_aleatorias = random.sample(palavras, 10)

#print(palavras_aleatorias)

pontos = 0
tic = time.perf_counter()
for palavras in palavras_aleatorias:
    print(palavras)
    entrada = input()
    if entrada == palavras:
        pontos += 1
toc = time.perf_counter()
variavel = toc - tic
print(f'Você fez {pontos} pontos em {variavel:.0f} segundos')