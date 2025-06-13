from games import roleta
from games import caca_niquel as niquel

UserId = input('Login: ')
input('Senha: ')

conta = 10
while True:
    print('CASSINO ONLINE')
    print('Conta: R$ :' + str(conta))
    op = int(input('1. Roleta\n2. Caça-Níqueis\n3. Adicionar fundos\n0. Sair\n'))
    if op==1:
        conta = roleta.Game(conta)
    if op==2:
        conta = niquel.Nique(conta)
    if op==3:
        print('Adicionar fundos:\n')
        add = int(input('Valor: '))
        conta = conta + add
        print('\nBalanço total = ' + str(conta))
        input('Confirmar')
    if op==0:
        break



