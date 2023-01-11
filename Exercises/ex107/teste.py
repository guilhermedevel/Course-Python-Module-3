'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.'''

import moeda

v = float(input('Digite o preço: R$'))
print(f'A metade de R${v:.2f} é R${moeda.metade(v):.2f}')
print(f'O dobro de R${v:.2f} é R${moeda.dobro(v):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(v, porcentagem=10):.2f}')
print(f'Diminuindo 13%, temos R${moeda.diminuir(v, porcentagem=13):.2f}')
