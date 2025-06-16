from uteis import ferramentas as tools
from . import usuario

def loginConta(userAtual=None):
    """
    Módulo para o fluxo de login de um usuário validando suas credenciais
    Parâmetros:
        userAtual(User,opcional): Não utilizado
    Retornos:
        User | None: retorna o objeto de User se o login for completo e None se usuário decidir sair do login
    """
    userEncont = 0
    while True:
        tools.clean()
        print('0. Voltar\n')
        tentLogin = input('Digite seu login:\n').strip().lower()
        if tentLogin == '0':
            return None
        if not tentLogin:
            print('Login inválido\n')
            tools.sleep(1)
            continue
        #Loop para procurar o usuário no dicionário de usuários
        for user in usuario.User.all_users.values():
            if tentLogin == user.login:
                userEncont = user.nome
                break
        if not userEncont:
            print('Usuário não encontrado\n')
            tools.sleep(1)
            continue
        break
    #loop para verifição de senha
    while True:
        tools.clean()
        tentSenha = input('Digite sua senha\n').strip()
        if not tentSenha:
            print('Senha inválida\n')
            tools.sleep(1)
            continue
        if tentSenha != usuario.User.all_users[userEncont].senha:
            print('Senha incorreta\n')
            tools.sleep(1)
            continue
        break
    tools.clean()
    return usuario.User.all_users[userEncont] 

def addConta(userAtual=None):
    """
    Módulo para o fluxo de criação de uma nova conta de usuário
    Parâmetros:
        userAtual(User,opcional): Não utilizado
    Retornos:
        User: retorna o objeto de User recém criado
    """
    while True:
        tools.clean()
        login = input('Digite um login para a conta\n').strip().lower()
        if not login:
            print('Login inválido\n')
            tools.sleep(1)
            continue
        existe = False
        #loop para obter um login válido e único
        for user in usuario.User.all_users.values():
            if login == user.login:
                existe = True
                break
        if existe :
            print('Login já existente\n')
            tools.sleep(1)
            continue
        break
    #loop para obter uma senha válida
    while True:
        tools.clean()
        senha = input('Digite uma senha para a conta\n').strip()
        if not senha:
            print('Senha inválida\n')
            tools.sleep(1)
            continue
        break
    #loop para obter um nome válido e único
    while True:
        tools.clean()
        nome = input('Digite um nome para a conta\n').strip()
        if not nome :
            print('Nome inválido\n')
            tools.sleep(1)
            continue
        if nome in usuario.User.all_users.keys():
            print('Nome já existente\n')
            tools.sleep(1)
            continue
        break
    usuario.User(login, senha, nome)
    return usuario.User.all_users[nome]


def rmConta(userAtual):
    """
    Módulo para o fluxo de exclusão de conta
    Parâmetros:
        userAtual(User): objeto User que é usuário logado e ele que será excluído do sistema
    Retornos:
        'Sessão Terminada': para quando o usuário seja excluido o sistema saiba que o usuario foi desconectado
        None: para quando o usuário decedir cancelar a ação não alterando nada
    """
    nome = userAtual.nome
    while True:
        tools.clean()
        resp = int(input('Deseja deletar sua conta?\n1. Confirmar\n2. Cancelar\n'))
        if resp == 1:
            del usuario.User.all_users[nome]
            input('Usuário Excluido com sucesso\nPresione Enter para continuar\n')
            return 'Sessão Terminada'
        if resp == 2:
            return None
        print('Resposta inválida\n')
        tools.sleep(1)
