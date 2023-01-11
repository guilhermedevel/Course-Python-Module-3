'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

numbers = list()
for counter in range(0, 5):
    numbers.append(int(input(f'Digite o {counter + 1}º valor: ')))
print('=-' * 30)
print(f'Você digitou os valores: {numbers}')
print(f'O maior valor digitado foi {max(numbers)} nas posições ', end='')
for ind, value in enumerate(numbers):
    if value == max(numbers):
        print(f'{ind + 1}...', end='')
print()
print(f'O menor valor digitado foi {min(numbers)} nas posições ', end='')
for ind, value in enumerate(numbers):
    if value == min(numbers):
        print(f'{ind + 1}...', end='')
print()
