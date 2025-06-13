import random
from os import system, name
import sys

def clean():                    #função que limpa o texto do terminal
	if name == 'nt':            #propósito organizaçional e de apresentação
		_ = system('cls')       #ou seja, só pra ficar bonitinho 
	else:                       #(não tá funcionando perfeitamente e eu não sei o pq, vou dar uma pesquisada)
		_ = system('clear')
		
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def Roll():
	symbols = ['©', '®', '¤', '¢', '£', '¶', '$', '¥', '&']
	result = ['a', 'b', 'c']
	for x in range(3):
		y = random.randint(0, 8)
		result[x] = symbols[y]
	print(result)
	return result
	

def Nique(conta):
	conta = int(conta)
	print('Seu saldo ' + str(conta))
	valor = int(input('\nFaça sua aposta: '))
	if valor > conta:
		print('Fundos insuficientes')
		sys.exit()
	if valor < conta:
		conta = conta - valor
	result = Roll()
	if result[0] == result[1] and result[1] == result[2]:
		conta = conta * 10
	if result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
		conta = conta * 2
	return conta

	