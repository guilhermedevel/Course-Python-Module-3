'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de
forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.'''


def leiaInt(frase):
    ok = False
    valor = 0
    while True:
        n = str(input(frase))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
