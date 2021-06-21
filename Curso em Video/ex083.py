# VALIDANDO EXPRESSOES MATEMATICAS
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


ex = input('Digite uma expressao qualquer: ')

aberto = 0
fechado = 0

x = ''
for c in range(len(ex)):
    cu = ex[c]
    if cu == '(':
        aberto += 1
    if cu == ')':
        fechado += 1

if aberto == fechado:
    print('Essa expressão é valida')
else:
    print('Essa expressão é invalida')


