def leiaDinheiro(msg):
    valido = False
    while not valido:
        resp = str(input(msg)).replace(',', '.').strip()
        if resp.isalpha() or resp == '':
            print(f'\033[0;31mERRO: \"{resp}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(resp)


def leiaInt(frase):
    while True:
        try:
            valor = int(input(frase))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return valor


def leiaFloat(frase):
    while True:
        try:
            real = float(input(frase))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
            return float(0)
        else:
            return real

