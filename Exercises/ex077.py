'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

vocabulary = ('aprender', 'programar', 'linguagem',
              'python', 'curso', 'gratis', 'estudar',
              'praticar', 'trabalhar', 'mercado',
              'programador', 'futuro')
for word in vocabulary:
    print(f'\nNa palavra {word.upper()} temos', end=' ')
    for lyrics in word:
        if lyrics in 'aeiuo':
            print(f'{lyrics}', end=' ')
