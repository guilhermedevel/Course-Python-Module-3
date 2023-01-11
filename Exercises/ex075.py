'''Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

values = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os números: {values}')
print(f'O número 9 apareceu {values.count(9)} vezes.')
if 3 in values:
    print(f'O número 3 apareceu na {values.index(3)+1}ª posição.')
else:
    print('O número 3 não faz parte dessa sequência.')
print('Os valores pares digitados foram: ', end='')
for number in values:
    if number % 2 == 0:
        print(f'{number}', end=' ')

