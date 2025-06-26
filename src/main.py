#Importação dos módulos e classes de seus respectivos pacotes
from interface import menu                                      
from contas import usuario
from jogos import caca_niquel as nique
from jogos import roleta
from uteis import ferramentas as tools
from contas import acesso

#Usuário para teste Login = admin senha = admin
admin = usuario.User("admin","admin","admin")
admin.saldo = 9999.99
# -------------------- Montagem da Estrutura de Menus --------------------------------

#Define a estrutura do menu de acesso (Usuário não logado)
menuAcesso = menu.Menu('Cassino Online\n')
menuAcesso.adFilho('1', menu.Menu('1. Fazer login\n', acesso.loginConta))
menuAcesso.adFilho('2' ,menu.Menu('2. Criar conta\n', acesso.addConta))
menuAcesso.adFilho('3', menu.Menu('3. Sair\n', tools.exit))

#Define a estrutura do menu principal (Usuário logado)
menuPrinc = menu.Menu('Bem Vindo ao Cassino Online\n')
menuPrinc.adFilho('1', menu.Menu('1. Jogar\n'))
menuPrinc.adFilho('2', menu.Menu('2. Opcões\n'))
menuPrinc.adFilho('3', menu.Menu('3. Sair\n', tools.exit))

#Define os submenus que são filhos do menu principal
menuJogo = menuPrinc.menuFilhos['1']
menuJogo.adFilho('1', menu.Menu('1. Roleta\n', roleta.jogar))
menuJogo.adFilho('2', menu.Menu('2. Caça-níqueis\n', nique.jogar))
menuOpt = menuPrinc.menuFilhos['2']
menuOpt.adFilho('1', menu.Menu('1. Depositar\n' , usuario.User.depositar))
menuOpt.adFilho('2', menu.Menu('2. Sacar\n', usuario.User.sacar))
menuOpt.adFilho('3', menu.Menu('3. Excluir conta\n', acesso.rmConta))

# -------------------- Loop principal --------------------------------

#Loop gerencia o estado da sessão do usuário
#1. Navega pelo menu de acesso. Se o usuário criar conta ou logar, 'logado' recebe o objeto do usuário
#2. Se 'logado' for um objeto de usuário (True) é iniciado o menu principal
#3. Se o usuário excluir a conta durante o menu principal ou sair dele o logado recebe None, e o ciclo recomeça do menu acesso
while True:
    logado = menu.navegar(menuAcesso)
    if logado:
        logado = menu.navegar(menuPrinc, logado)
