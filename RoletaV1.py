import random
from os import system, name

def clean():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

clean()

print('ROLETA ONLINE')
input('Aperte qualquer botão para jogar')

clean()

for x in range(100):
    if x%2==0 and x!=0 and x!=1:
        prRed(x)
    if x%2==1 and x!=0 and x!=1:
        prBlack(x)
    if x==1:
        prGreen(x)

input('Selecione em quais valores deseja apostar')

clean()

ganhador = random.randint(1, 99)

print('O Valor sorteado é: ')
print(ganhador)