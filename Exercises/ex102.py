'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um
valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(num, show=False):
    '''
    -> Função para calcular o fatorial de um número.
    :param num: número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: o valor do fatorial de um número n.
    '''
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c == 1:
                print(f' = ', end='')
            else:
                print(f' x ', end='')
    return f


# Programa Principal
print(fatorial(6, show=True))
help(fatorial)
