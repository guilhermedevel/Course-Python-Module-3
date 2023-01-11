'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre
a lista ordenada na tela.'''

values = list()
for num in range(0, 5):
    n = int(input('Digite um valor: '))
    if num == 0 or n > values[-1]:
        values.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(values):
            if n <= values[pos]:
                values.insert(pos, n)
                print(f'Adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram: {values}')
