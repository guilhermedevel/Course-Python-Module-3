'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre
os valores pares e ímpares em ordem crescente.'''

general = [[], []]
for cont in range(1, 8):
    num = int(input(f'Digite o {cont}º valor: '))
    if num % 2 == 0:
        general[0].append(num)
    else:
        general[1].append(num)
general[0].sort()
general[1].sort()
print(f'Os valores pares digitados foram: {general[0]}')
print(f'Os valores ímpares digitados foram: {general[1]}')
