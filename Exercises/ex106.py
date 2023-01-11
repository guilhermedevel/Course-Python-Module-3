'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
'FIM', o programa se encerrará. Importante: use cores.'''

from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[97;41m',   # 1 - vermelho
     '\033[97;42m',   # 2 - verde
     '\033[97;43m',   # 3 - amarelo
     '\033[97;44m',   # 4 - azul
     '\033[97;45m',   # 5 - roxo
     '\033[30;107m'   # 6 - branco
     )


def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", cor=4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor=2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO', cor=1)
        break
    ajuda(comando)
