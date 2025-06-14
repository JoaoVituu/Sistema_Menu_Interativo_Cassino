class User : #Definição da classe
    all_users = {} #Dicionario que armazena as instancias do objeto
    def __init__ (self, login, senha, nome): #metodo construtor de classe
        self.login = login
        self.senha = senha
        self.nome = nome
        self.saldo = 10.00 
        self.histBet = [] #historico das apostas
        User.all_users[nome] = self #armazena a instancia no indice nome que seria o nick da pessoa
        
    #funcoes definidas dentro de class sao metodos para alterar os valores de atributos
    def depositar(self):
        while True:
            deposito = float(input('Digite o valor que deseja depositar:\n'))
            if deposito <= 0:
                print('Depósito inválido\n')
                continue
            saldoPrev = self.saldo + deposito
            resp = int(input('Saldo final será de R${:.2f}\n1. Confirmar\n2. Alterar depósito\n'.format(saldoPrev)))
            while resp != 1 and resp != 2:
                resp = int(input('Número inválido digite novamente\nSaldo final será de {:.2f}R$\n1. Confirmar\n2. Alterar depósito\n').format(saldoPrev))
            if resp == 1:
                self.saldo = saldoPrev
            if resp == 2:
                continue
            break

    def sacar(self):
        while True:
            saque = float(input('Saldo = {:.2f}\nDigite o valor a ser sacado\n'.format(self.saldo)))
            if 0 >= saque > self.saldo:
                print('saque inválido\n')
                continue
            saldoPrev = self.saldo - saque
            resp = int(input('Saldo Final: {}\n1. Confirmar\n2. Alterar Valor\n'.format(saldoPrev)))
            if resp == 1:
                self.saldo = saldoPrev
                break
            if resp == 2:
                continue

#Módulos
def adicionarUser():
    global userAtual 
    while True:
        login = input('Digite um login para a conta\n').strip().lower()
        if not login:
            print('Login inválido\n')
            continue
        existe = False
        for user in User.all_users.values():
            if login == user.login:
                existe = True
                break
        if existe :
            print('Login já existente\n')
            continue
        break
    while True:
        senha = input('Digite uma senha para a conta\n').strip()
        if not senha:
            print('Senha inválida\n')
            continue
        break
    while True:
        nome = input('Digite um nome para a conta\n').strip()
        if not nome :
            print('Nome inválido\n')
            continue
        if nome in User.all_users.keys():
            print('Nome já existente\n')
            continue
        break
    userAtual = nome
    User(login, senha, nome)

def loginUser():
    userEncont = None
    while True:
        tentLogin = input('Digite seu login:\n').strip().lower()
        if not tentLogin:
            print('Login inválido\n')
            continue
        for user in User.all_users.values():
            if tentLogin == user.login:
                userEncont = user.nome
                break
        if not userEncont:
            print('Usuário não encontrado\n')
            continue
        break
    while True:
        tentSenha = input('Digite sua senha\n').strip()
        if not tentSenha:
            print('Senha inválida\n')
            continue
        if tentSenha != User.all_users[userEncont].senha:
            print('Senha incorreta\n')
            continue
        break
    print('Bem vinda de volta {}\n'.format(userEncont))
    return userEncont

def excluirUser(nome):
    while True:
        resp = int(input('Deseja deletar sua conta?\n1. Confirmar\n2. Cancelar\n'))
        if resp == 1:
            del User.all_users[nome]
            break
        if resp == 2:
            break
        print('Resposta inválida\n')

#Teste adiciona 2 usuarios depois disso na conta2 faz um deposito e depois saca na conta2
#após isso faz um login para trocar de conta como so foram adicionado 2 contas vc so pode voltar pra primeira 
#depois exclui a conta atual a primeira conta e printa o nicks dos usuarios no sistema ou seja so a segunda conta
userAtual = None
adicionarUser() 
print(userAtual)
user1 = userAtual
print(User.all_users[userAtual].saldo)
adicionarUser()
print(userAtual)
print(User.all_users[userAtual].saldo)
User.depositar(User.all_users[userAtual])
print(User.all_users[user1].saldo)
print(User.all_users[userAtual].saldo)
User.sacar(User.all_users[userAtual])
userAtual = loginUser()
excluirUser(userAtual)
print(User.all_users.keys())