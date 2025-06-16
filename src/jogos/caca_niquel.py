import random
from uteis import ferramentas as tools
def Roll():
	symbols = ['©', '®', '¤', '¢', '£', '¶', '$', '¥', '&']
	result = ['a', 'b', 'c']
	for x in range(3):
		y = random.randint(0, 8)
		result[x] = symbols[y]
	print(result)
	return result

def jogar(user):
	tools.clean()
	conta = user.saldo
	print('Seu saldo ' + str(conta))
	valor = int(input('\nFaça sua aposta: '))
	if valor > conta:
		print('Fundos insuficientes')
		tools.sleep(1)
		return
	else: 
		conta = conta - valor
	result = Roll()
	if result[0] == result[1] == result[2]:
		conta = conta + (valor * 10)
	elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
		conta = conta + (valor * 2)
	input('seu novo saldo é: {}R$\nPressione enter para continuar'.format(conta))
	user.saldo = conta

	