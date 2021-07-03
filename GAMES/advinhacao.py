import requests
import random
# entender como funciona as requests
# fazer parte que pergunta ao usuario uma letra
# verificar se foi digitado apenas uma letra
# colocar as letras que ja foram digitadas numa lista
# imprimir um * nas letras que aind anão foram digitadas
# fazer uma contagem de chances

url ='https://www.ime.usp.br/~pf/dicios/br-utf8.txt'

resposta = requests.get(url)
palavras = resposta.content.splitlines()

palavras = [ palavra.decode('utf-8')for palavra in palavras]

palavras_aleatorias = random.sample(palavras, 10)

