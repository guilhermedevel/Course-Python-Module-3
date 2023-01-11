'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

list = []
while True:
    list.append(int(input('Digite um valor: ')))
    again = str(input('Quer continuar? [S/N] ')).strip()[0]
    if again in 'nN':
        break
print(f'Você digitou {len(list)} elementos.')
list.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {list}')
if 5 in list:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
