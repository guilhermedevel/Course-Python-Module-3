'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sumPar = sumCol = largerLine = 0
for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^6}]', end=' ')
        if matrix[line][column] % 2 == 0:
            sumPar += matrix[line][column]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {sumPar}')

for line in range(0, 3):
    sumCol += matrix[line][2]
print(f'A soma dos valores da terceira coluna é {sumCol}')

for column in range(0, 3):
    if column == 0 or matrix[1][column] > largerLine:
        largerLine = matrix[1][column]
print(f'O maior valor da segunda linha é {largerLine}')
