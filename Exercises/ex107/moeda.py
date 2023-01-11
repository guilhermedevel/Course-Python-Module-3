def aumentar(valor, porcentagem=1):
    novovalor = valor + (valor*porcentagem/100)
    return novovalor


def diminuir(valor, porcentagem=1):
    novovalor = valor - (valor*porcentagem/100)
    return novovalor


def metade(valor):
    m = valor/2
    return m


def dobro(valor):
    d = valor*2
    return d
