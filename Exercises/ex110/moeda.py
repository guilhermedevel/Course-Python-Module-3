def aumentar(valor=0, porcentagem=0, conv=False):
    novovalor = valor + (valor*porcentagem/100)
    return novovalor if conv is False else moeda(novovalor)


def diminuir(valor=0, porcentagem=0, conv=False):
    novovalor = valor - (valor*porcentagem/100)
    return novovalor if conv is False else moeda(novovalor)


def metade(valor=0, conv=False):
    m = valor/2
    return m if not conv else moeda(m)


def dobro(valor=0, conv=False):
    d = valor*2
    return d if not conv else moeda(d)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def resumo(valor=0, aumento=10, diminuindo=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{diminuindo}% de redução: \t{diminuir(valor, diminuindo, True)}')
    print('-' * 30)
