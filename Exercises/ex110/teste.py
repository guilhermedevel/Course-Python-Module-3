'''Exercício Python 110: Adicione ao módulo moeda.py criado nos desafios anteriores, uma função
chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no
módulo criado até aqui.'''

from ex110 import moeda

v = float(input('Digite o preço: R$'))
moeda.resumo(v, 20, 12)
