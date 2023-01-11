'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as
dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m².')


#programa principal
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)

