'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita
que o usuário possa mostrar as notas de cada aluno individualmente.'''

turma = list()
temp = list()
final = list()
while True: #captação dados alunos
    temp.append(str(input('Nome: ')).strip().capitalize())
    temp.append(float(input('Nota 1: ')))
    temp.append((float(input('Nota 2: '))))
    turma.append(temp[:])
    temp.clear()
    exit = str(input('Quer continuar? [S/N]: ')).strip()
    if exit in 'nN':
        break

for aluno in turma: #calculando a média de todos os alunos da turma
    media = (aluno[1] + aluno[2]) / 2
    final.append(media)

print('=-' * 30)
print('Nº   NOME         MÉDIA')
print('-' * 30)

for cont in range(0, len(turma)): #exibindo boletim
    print(f'{cont:<4} {turma[cont][0]:10} {final[cont]:>6.2f}')

print('-' * 30)

while True: #exibindo notas individuais
    individual = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if individual == 999:
        break
    if individual <= len(turma) - 1:
        print(f'As notas de {turma[individual][0]} são: {turma[individual][1:]}')
    print('-' * 30)
