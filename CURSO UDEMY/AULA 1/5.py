frase = 'O rato roeu a roupa do rei de roma'
tamanho = len(frase)
contador = 0
nova_string = ''

print(frase)


while True:
    input_do_usuario = input('Qual letra voce deseja colocar maiuscula: ')
    if input_do_usuario not in frase:
        print('Escolha uma letra que esteja no texto')
    else:
        break

while contador < tamanho:
    letra = frase[contador]
    
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else: 
        nova_string += letra
    contador += 1

print(nova_string)