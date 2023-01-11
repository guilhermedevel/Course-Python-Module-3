'''Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint
raffle = (randint(1, 10), randint(1, 10), randint(1, 10),
          randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for number in raffle:
    print(f'{number}', end=' ')
print(f'\nO maior valor sorteado foi: {max(raffle)}')
print(f'O menor valor sorteado foi: {min(raffle)}')
