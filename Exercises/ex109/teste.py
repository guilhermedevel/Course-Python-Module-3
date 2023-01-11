'''Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função
moeda(), desenvolvida no desafio 108.'''

from ex109 import moeda

v = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(v)} é {moeda.metade(v, True)}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.dobro(v, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(v, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(v, 13, True)}')
