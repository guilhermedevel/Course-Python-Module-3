'''Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado.'''

from ex108 import moeda

v = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(v)} é {moeda.moeda(moeda.metade(v))}')
print(f'O dobro de {moeda.moeda(v)} é {moeda.moeda(moeda.dobro(v))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(v, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(v, 13))}')
