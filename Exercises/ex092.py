'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
com quantos anos a pessoa vai se aposentar.'''

from datetime import date
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: '))
trabalhador['idade'] = date.today().year - nascimento
trabalhador['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['CTPS'] > 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salário'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - date.today().year)
for k, v in trabalhador.items():
    print(f' - {k} tem o valor {v}.')
