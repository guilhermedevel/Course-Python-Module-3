'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

general = list()
par = list()
odd = list()
while True:
    general.append(int(input('Digite um valor: ')))
    ask = str(input('Quer continuar? [S/N] '))
    if ask in 'Nn':
        break
for num in general:
    if num % 2 == 0:
        par.append(num)
    else:
        odd.append(num)
print(f'A lista completa é {general}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {odd}')
