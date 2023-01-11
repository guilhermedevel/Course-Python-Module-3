def aumentar(valor=0, porcentagem=0):
    novovalor = valor + (valor*porcentagem/100)
    return novovalor


def diminuir(valor=0, porcentagem=0):
    novovalor = valor - (valor*porcentagem/100)
    return novovalor


def metade(valor=0):
    m = valor/2
    return m


def dobro(valor=0):
    d = valor*2
    return d


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')

