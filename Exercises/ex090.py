'''Exercício Python 090: Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
