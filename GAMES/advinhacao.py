# Jogo de adivinhação
import requests
import random

# palavra = 'perfume'
digitadas = []
chances = 5

url = 'https://www.ime.usp.br/~pf/dicios/br-utf8.txt'

resposta = requests.get(url)

u = resposta.content.splitlines()

u = [palavra.decode('utf-8') for palavra in u]

palavras = random.sample(u, 1)

while True:
    # if chances <= 0:
    #     print('suas chances acabaram, voce perdeu!')
    #     break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in palavras:
        print(f'A letra {letra} existe na palavra secreta')

    else:
        print(f' A letra {letra} Nao existe na palavra secreta')
        digitadas.pop()

    temp = ''

    for letra_secreta in palavras:
        if letra_secreta in digitadas:
            temp += letra_secreta

        else:
            temp += '*'

    if temp == palavras:
        print(f'Que legal, Voce ganhou! A palavra é: {temp}')
        break
    else:
        print(f'A palavra secreta esta assim: {temp}')

    if letra not in palavras:
        chances -= 1

    print(f'Voce ainda tem {chances} chances.')

    print(palavras)
