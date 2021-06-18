# TUPLAS COM TIMES DE FUTEBOL
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino', 'Ceará', 'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo', 'Sport')
print('~' * 300)
print(f'Lista de times do Brasileirão: {times}')
print('~' * 300)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('~' * 100)
print(f'Os 4 ultimos são: {times[16:]}')
posição = times.index('Chapecoense')
print('~' * 100)
print(f'A chapecoense esta em {posição}º lugar!')
