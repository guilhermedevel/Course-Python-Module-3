'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

cadastros = list()
temp = dict()
somaidades = mediaidade = 0

while True:
    temp['nome'] = str(input('Nome: ')).strip().title()
    while True:
        temp['sexo'] = str(input('Sexo: [M/F] ').strip().upper()[0])
        if temp['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas M ou F. ')
    temp['idade'] = int(input('Idade: '))
    somaidades += temp['idade']
    cadastros.append(temp.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-='*30)
print(f'A) Ao todo temos {len(cadastros)} pessoas cadastradas.')

mediaidade = somaidades / len(cadastros)
print(f'B) A média de idade é de {mediaidade:.2f} anos.')

print(f'C) As mulheres cadastradas foram: ', end='')
for pessoa in cadastros:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end='')
print()

print('D) Lista das pessoas que estão acima da média:')
for pessoa in cadastros:
    if pessoa['idade'] > mediaidade:
        print('    ', end='')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
