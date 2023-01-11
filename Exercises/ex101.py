'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


#Programa principal
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
