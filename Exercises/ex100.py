'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções
chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro
da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print()


def somaPar(lista):
    spar = 0
    for num in lista:
        if num % 2 == 0:
            spar += num
    print(f'Somando os valores pares de {lista}, temos {spar}')


#Programa principal

numeros = list()
sorteia(numeros)
somaPar(numeros)

