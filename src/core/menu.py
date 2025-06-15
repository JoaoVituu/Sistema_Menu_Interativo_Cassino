from os import system,name
import sys
import time
import usuario

class Menu:
    def __init__(self,text=None, acao=None):
        self.text = text
        self.acao = acao
        self.menuPai = None
        self.menuFilhos = {}
    def adFilho(self,tecla, noFilho):
        self.menuFilhos[tecla] = noFilho
        noFilho.menuPai = self


def clean():                 
	if name == 'nt':           
		_ = system('cls')       
	else:                       
		_ = system('clear')

def navegar(menu, userAtual=None):
        while True:
            clean()
            texto = menu.text 
            if '.' in texto:
                texto = texto[2:]
            print(texto)
            if userAtual and menu == menuPrinc:
                print('{}\nSaldo: {:.2f}\n'.format(userAtual.nome, userAtual.saldo))
            for opt in menu.menuFilhos.values():
                print(opt.text)
            if menu.menuPai:
                print('0. Voltar')
            resp = input().strip()
            if resp == '0' and menu.menuPai:
                menu = menu.menuPai
                continue
            menuProx = menu.menuFilhos.get(resp)
            if not menuProx:
                print('Opção inválida')
                time.sleep(1.5)
                continue
            if menuProx.acao:
                resultado = menuProx.acao(userAtual)
                if resultado == 'Sessão Encerrada':
                    return None
                elif resultado:
                    return resultado
            elif menuProx.menuFilhos:
                menu = menuProx
            else:
                print('Fatal Error')
                time.sleep(1.5)
                

userAtual = None
def loginMenu(userAtual):
    userEncont = 0
    while True:
        clean()
        print('0. Voltar')
        tentLogin = input('Digite seu login:\n').strip().lower()
        if tentLogin == '0':
            return None
        if not tentLogin:
            print('Login inválido\n')
            time.sleep(1.5)
            continue
        for user in usuario.User.all_users.values():
            if tentLogin == user.login:
                userEncont = user.nome
                break
        if not userEncont:
            print('Usuário não encontrado\n')
            time.sleep(1.5)
            continue
        break
    while True:
        clean()
        tentSenha = input('Digite sua senha\n').strip()
        if not tentSenha:
            print('Senha inválida\n')
            time.sleep(1.5)
            continue
        if tentSenha != usuario.User.all_users[userEncont].senha:
            print('Senha incorreta\n')
            time.sleep(1.5)
            continue
        break
    clean()
    print('Bem vinda de volta {}\n'.format(userEncont))
    return usuario.User.all_users[userEncont]

def cadastro(userAtual):
    while True:
        clean()
        login = input('Digite um login para a conta\n').strip().lower()
        if not login:
            print('Login inválido\n')
            time.sleep(1.5)
            continue
        existe = False
        for user in usuario.User.all_users.values():
            if login == user.login:
                existe = True
                break
        if existe :
            print('Login já existente\n')
            time.sleep(1.5)
            continue
        break
    while True:
        clean()
        senha = input('Digite uma senha para a conta\n').strip()
        if not senha:
            print('Senha inválida\n')
            time.sleep(1.5)
            continue
        break
    while True:
        clean()
        nome = input('Digite um nome para a conta\n').strip()
        if not nome :
            print('Nome inválido\n')
            time.sleep(1.5)
            continue
        if nome in usuario.User.all_users.keys():
            print('Nome já existente\n')
            time.sleep(1.5)
            continue
        break
    usuario.User(login, senha, nome)
    return usuario.User.all_users[nome]

def excluirConta(userAtual):
    nome = userAtual.nome
    while True:
        clean()
        resp = int(input('Deseja deletar sua conta?\n1. Confirmar\n2. Cancelar\n'))
        if resp == 1:
            del usuario.User.all_users[nome]
            input('Usuário Excluido com sucesso\nPresione Enter para continuar\n')
            return 'Sessão Terminada'
        if resp == 2:
            return None
        print('Resposta inválida\n')
        time.sleep(1.5)


def deposito(userAtual):
    usuario.User.depositar(userAtual)

def saque(userAtual):
    usuario.User.sacar(userAtual)

def roletaIniciar(userAtual):
    from games import roleta
    saldo = userAtual.saldo
    userAtual.saldo = roleta.jogar(saldo)

def niqueIniciar(userAtual):
    from games import caca_niquel as nique
    saldo = userAtual.saldo
    userAtual.saldo = nique.jogar(saldo)

acesso = Menu('Cassino Online\n')
acesso.adFilho('1', Menu('1. Fazer login\n', loginMenu))
acesso.adFilho('2' ,Menu('2. Criar conta\n', cadastro))
acesso.adFilho('3', Menu('3. Sair\n', sys.exit))

menuPrinc = Menu('Bem Vindo ao Cassino Online0\n')
menuPrinc.adFilho('1', Menu('1. Jogar\n'))
menuPrinc.adFilho('2', Menu('2. Opcões\n'))
menuPrinc.adFilho('3', Menu('3. Sair\n', sys.exit))

menuJogo = menuPrinc.menuFilhos['1']
menuJogo.adFilho('1', Menu('1. Roleta\n', roletaIniciar))
menuJogo.adFilho('2', Menu('2. Caça-níqueis', niqueIniciar))

menuOpt = menuPrinc.menuFilhos['2']
menuOpt.adFilho('1', Menu('1. Depositar\n' ,deposito))
menuOpt.adFilho('2', Menu('2. Sacar\n', saque))
menuOpt.adFilho('3', Menu('3. Excluir conta\n', excluirConta))

while True:
    userAtual = navegar(acesso, userAtual)
    if userAtual:
        userAtual = navegar(menuPrinc, userAtual)


