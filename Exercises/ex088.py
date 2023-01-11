'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para
cada jogo, cadastrando tudo em uma lista composta.'''

from time import sleep
from random import randint
print('-'*30)
print('       JOGA NA MEGA SENA       ')
print('-'*30)
amount = int(input('Quantos jogos você quer que eu sorteie? ')) #quantidade de jogos total
game = []
num = cont = 0
print(f'-=-=-= SORTEANDO {amount} JOGOS -=-=-=')
sleep(0.5)
for c in range(0, amount):
    while True:
        num = randint(1, 60)
        if num not in game:
            game.append(num)
            cont += 1
        if cont == 6:
            game.sort()
            print(f'Jogo {c+1}: {game}')
            cont = 0
            game.clear()
            sleep(1)
            break
