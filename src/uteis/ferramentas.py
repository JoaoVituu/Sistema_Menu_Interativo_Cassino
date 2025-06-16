from os import system,name
import time
import sys

def clean():                    #função que limpa o texto do terminal
	if name == 'nt':            #propósito organizaçional e de apresentação
		_ = system('cls')       #ou seja, só pra ficar bonitinho 
	else:                       #(não tá funcionando perfeitamente e eu não sei o pq, vou dar uma pesquisada)
		_ = system('clear')
def sleep(s):
	time.sleep(s)
def exit(user=None):
	sys.exit()
	#funções que dão cor pro texto
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
