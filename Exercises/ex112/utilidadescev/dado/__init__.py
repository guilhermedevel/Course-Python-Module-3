def leiaDinheiro(msg):
    valido = False
    resp = ''
    while not valido:
        resp = str(input(msg)).replace(',', '.').strip()
        if resp.isalpha() or resp == '':
            print(f'\033[0;31mERRO: \"{resp}\" é um preço inválido!\033[m')
        else:
            valido = True
    return float(resp)


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

