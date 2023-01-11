'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

from time import sleep


def maior(*valores):
    print('-='*30)
    tam = len(valores)
    print('Analisando os valores passados...')
    larger = 0
    for cont, num in enumerate(valores):
        print(num, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            larger = num
        else:
            if num > larger:
                larger = num
    sleep(1)
    print(f'Foram informados {tam} valores ao todo.', flush=True)
    sleep(2)
    print(f'O maior valor informado foi {larger}.', flush=True)
    sleep(2)


#Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
