'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = dict()
partidas = list()
time = list()

while True:
    jogador['Nome'] = str(input('Nome do Jogador: ')).capitalize().strip()
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(jogador['Gols'])
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp == 'N':
        break

print('-' * 50)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-' * 50)

for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for dado in v.values():
        print(f'{str(dado):<15} ', end='')
    print()
print('-' * 50)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para encerrar) '))
    if busca == 999:
        break
    elif busca >= len(time):
        print(f'Erro! Não existe jogador com o código {busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["Nome"]}:')
        for k, v in enumerate(time[busca]['Gols']):
            print(f'    Na partida {k+1} fez {v} gols.')
    print('-' * 50)
print('<< Volte Sempre >>')
