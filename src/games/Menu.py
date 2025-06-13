import RoletaV1 as r
import CacaNiqueis as c

UserId = input('Login: ')
input('Senha: ')

conta = 10

print('ROLETA ONLINE')
print('Conta: R$ :' + str(conta))
op = int(input('1. Roleta\n2. Caça-Níqueis\n3. Adicionar fundos\n'))
if op==1:
    r.Game(conta)
if op==2:
    c.Nique(conta)
if op==3:
    print('Adicionar fundos:\n')
    add = int(input('Valor: '))
    conta = conta + add
    print('\nBalanço total = ' + str(conta))
    input('Confirmar')



