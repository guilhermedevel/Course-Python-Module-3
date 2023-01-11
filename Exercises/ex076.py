'''Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados
em forma tabular.'''

catalog = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9,
           'Estojo', 25, 'Transferidor', 4.2, 'Compasso',
           9.99, 'Mochila', 120.32, 'Canetas', 22.3,
           'Livro', 34.9)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, len(catalog)):
    if item % 2 == 0:
        print(f'{catalog[item]:.<30}',end='')
    else:
        print(f'R${catalog[item]:>6.2f}')
print('-' * 40)
