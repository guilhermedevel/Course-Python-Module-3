'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

people = list()
data = list()
heavy = light = 0

while True:
    data.append(str(input('Nome: ')).strip().title())
    data.append(float(input('Peso: ')))
    if len(people) == 0:
        heavy = light = data[1]
    else:
        if data[1] > heavy:
            heavy = data[1]
        elif data[1] < light:
            light = data[1]
    people.append(data[:])
    data.clear()
    ask = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if ask in 'N':
        break

print(f'Ao todo, você cadastrou {len(people)} pessoas.')
print(f'O maior peso foi de {heavy}Kg. Peso de : ', end='')
for person in people:
    if person[1] == heavy:
        print(f'[{person[0]}] ', end='')
print()
print(f'O menor peso foi de {light}Kg. Peso de: ', end='')
for person in people:
    if person[1] == light:
        print(f'[{person[0]}] ', end='')
