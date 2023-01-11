'''Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo
computador usado.'''

from urllib.error import URLError
from urllib.request import urlopen

try:
    site = urlopen('http://www.pudim.com.br/')
except URLError:
    print('\033[31mSite do Pudim não está acessível no momento.\033[m')
else:
    print('\033[34mConsegui acessar o site do Pudim.\033[m')
    print(site.read())
    
