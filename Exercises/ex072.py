'''Exercício Python 072: Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''

score = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'catorze', 'quinze', 'dezeseis',
         'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    interaction = int(input('Digite um número entre 0 e 20: '))
    if interaction > 20 or interaction < 0:
        print('Tente novamente.', end=' ')
    if 0 <= interaction <= 20:
        print(f'Você digitou o número {score[interaction]}.')
    interactionTwo = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while interactionTwo not in 'SN':
        interactionTwo = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if interactionTwo == 'N':
        break
