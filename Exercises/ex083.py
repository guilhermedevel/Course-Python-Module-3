'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expression = str(input('Digite a expressão: '))
stack = list()
for symbol in expression:
    if symbol == '(':
        stack.append('(')
    elif symbol == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break
if len(stack) == 0:
    print('Expressão válida!')
else:
    print('Expressão inválida!')
