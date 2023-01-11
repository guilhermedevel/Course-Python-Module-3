from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')      # 'rt' significa read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')    # 'wt+' significa write text e criar o arquivo caso não exista
        a.close()
    except:
        print('Houve um ERRO não criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')          # 'at' significa Append Text
    except:
        print('ERRO ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao escrever os dados!')
        else:
            print(f'Cadastro de {nome} adicionado com sucesso!')
            a.close()
