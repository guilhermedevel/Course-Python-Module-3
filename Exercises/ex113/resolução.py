'''Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma
função leiaFloat() com a mesma funcionalidade.'''

from ex113.utilidadescev import dado

inteiro = dado.leiaInt('Digite um número inteiro: ')
real = dado.leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro}'
      f'\nO valor real digitado foi {real}')
