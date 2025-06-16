#Importação de módulos
from uteis import ferramentas as tools

#Classe que representa um único menu (ou nó) na árvore de navegação
class Menu:
    
    def __init__(self,text=None, acao=None):
        """
        Inicializa um nó de menu

        Parâmetros:
            text(string, opcional): Texto a ser exibido para este menu
            acao(function, opcional): A função a ser executada quando o menu é escolhido
        """
        self.text = text
        self.acao = acao
        self.menuPai = None
        self.menuFilhos = {}

    
    def adFilho(self,tecla, noFilho):
        """
        Adciona um submenu (nó filho) ao menu referenciado

        Parâmetros:
            tecla(str): A tecla que o usuário escolhe para acessar o nó filho
            noFilho(Menu): o objeto Menu que representa o filho
        """
        self.menuFilhos[tecla] = noFilho
        noFilho.menuPai = self


def navegar(menu, logado=None):
        """
        Controla o loop de navegação interativa para o menu referenciado
        Exibe o menu, suas opções, processa as entradas do usuário para navegação de submenus,
        volta para menu pai ou executa as ações de menu

        Parâmetros:
            menu(Menu): objeto Menu de onde a navegação se inciaria (Raiz)
            logado(Menu, opcional): objeto User que referencia o usuário logado no momento
        
        Retornos:
            Pode retornar o objeto User que referencia o usuário logado no momento (usuário criou uma conta ou fez o login)
            Pode retornar None (usuário exclui a conta)
        """
        while True:
            tools.clean()
            texto = menu.text 
            if '.' in texto: 
                texto = texto[3:]
            print(texto)
            if logado:
                print('{}\nSaldo: {:.2f}\n'.format(logado.nome, logado.saldo))
            for opt in menu.menuFilhos.values():
                print(opt.text) 
            if menu.menuPai: 
                print('0. Voltar\n')
            resp = input().strip()
            if resp == '0' and menu.menuPai: 
                menu = menu.menuPai
                continue
            else:
                menuProx = menu.menuFilhos.get(resp)
            if not menuProx: 
                input('Opção inválida\nPressione Enter para tentar Novamente\n')
                continue
            if menuProx.acao: 
                resultado = menuProx.acao(logado) 
                if resultado == 'Sessão Encerrada': 
                    return None
                elif resultado:
                    return resultado
            elif menuProx.menuFilhos: 
                menu = menuProx
            else: 
                print('Fatal Error')
                exit()
                


