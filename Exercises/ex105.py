'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''


def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''
    dicionario = dict()
    dicionario['total'] = len(n)
    maior = menor = soma = 0
    for c, v in enumerate(n):
        soma += v
        if c == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            elif v < menor:
                menor = v
    media = soma / len(n)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['media'] = media
    if sit:
        if media < 5:
            dicionario['situação'] = 'RUIM'
        elif 5 <= media < 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'BOA'
    return dicionario


# Programa principal
resp = notas(5.6, 7.5, 8, 9, sit=True)
print(resp)
help(notas)

