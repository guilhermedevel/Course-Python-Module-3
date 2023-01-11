def aumentar(valor=0, porcentagem=0, conv=False):
    """
    > Função para aumentar um valor numérico
    :param valor: valor a ser aumentado
    :param porcentagem: porcentagem do aumento
    :param conv: (opcional) True formata o valor em moeda
    :return: valor com o aumento
    """
    novovalor = valor + (valor*porcentagem/100)
    return novovalor if conv is False else moeda(novovalor)


def diminuir(valor=0, porcentagem=0, conv=False):
    """
    > Função para diminuir um valor numérico
    :param valor: valor a ser diminuído
    :param porcentagem: porcentagem da diminuição
    :param conv: (opcional) True formata o valor em moeda
    :return: valor com a diminuição
    """
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
