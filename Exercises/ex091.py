'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo
que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
jogadores['jogador 1'] = randint(1, 6)
jogadores['jogador 2'] = randint(1, 6)
jogadores['jogador 3'] = randint(1, 6)
jogadores['jogador 4'] = randint(1, 6)
ranking = list()
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING DOS JOGADORES":=^33}')
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
    