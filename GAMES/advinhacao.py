# Jogo de adivinhação
import requests
import random

#Gerar as palavras


resposta = requests.get(url)
u = resposta.content.splitlines()

u = [palavra.decode('utf-8') for palavra in u]



sorte = random.randint(0, 261797)

palavras_aleatorias = u[sorte]


chances = 5
digitadas = []


while True:
    if chances <= 0:
        print('Você perdeu!!!')
        print(f'A palavra era {palavras_aleatorias}.')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra not in palavras_aleatorias:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()
    else:
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    secreto_temporario = ''
    for letra_secreta in palavras_aleatorias:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == palavras_aleatorias:
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in palavras_aleatorias:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')

