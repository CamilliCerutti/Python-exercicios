variavel = ['luiz otavio', 'joaozinho', 'maria']

for valor in variavel:
    
    if valor.lower().startswith('j'):
        continue
    print(valor)
else:
    print('Nao existe uma palavra que começa com "j"')
