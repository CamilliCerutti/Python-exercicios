"""
OPERADOR TERNARIO
"""

logged_user = True

msg = 'Usuario logado.' if (logged_user == True) else 'Usuario precisa logar'

# if logged_user:
#     msg = 'Usuario logado'

# else:
#     msg = 'Usuario precisa logar'

print(msg)

idade = input('Qual a sua idade: ')

if not idade.isnumeric():
    print('Voce precisa digitar apenas numeros')

else:
    idade = int(idade)
    mensagem = 'Pode acessar' if idade >= 18 else 'nao pode acessar'

