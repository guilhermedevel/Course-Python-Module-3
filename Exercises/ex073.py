'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do São Paulo.'''

classification = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians',
         'Internacional', 'Athletico-PR', 'Atlético-MG', 'Santos',
         'América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaleza',
         'Botafogo', 'Ceará-SC', 'Cuiabá', 'Avaí', 'Coritiba', 'Atlético-GO',
         'Juventude')
print('-='*40)
print(f'Classificação dos times do Brasileirão: {classification}')
print('-='*40)
print(f'Os cinco primeiros colocados são: {classification[0:5]}')
print('-='*40)
print(f'Os quatro últimos são: {classification[-4:]}')
print('-='*40)
print(f'Times em ordem alfabética: {sorted(classification)}')
print('-='*40)
print(f'O São Paulo está na {classification.index("São Paulo")+1}ª colocação')
print('-='*40)
