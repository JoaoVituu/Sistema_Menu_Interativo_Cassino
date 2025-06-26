from uteis import ferramentas as tools

class User : 
    """
    Representa um usuário do sistema em que armazena suas credeciais, saldo e historico de apostas

    Atributos:
        login(string): login único do usuário
        senha(string): senha do usuário
        nome(string): nick name único do usuário
        saldo(float): valor que o usuário possui em conta
        histBet(list): pilha que contém as apostas anteriores
        all_users(dict): dicionário que armazena todas as instâncias criados da classe User 
        usando o atributo nome como suas respectivas keys
    """
    all_users = {} 

    def __init__ (self, login, senha, nome): 
        """
        Inicializa uma nova instância de User
        Parâmetros:
            login(string)
            senha(string)
            nome(string)
        """
        self.login = login
        self.senha = senha
        self.nome = nome
        self.saldo = 10.00  
        User.all_users[nome] = self 
        
    #Método que gerencia o processo de depósito para a conta do usuário
    def depositar(self):
        while True:
            tools.clean()
            deposito = float(input('Digite o valor que deseja depositar:\n'))
            if deposito <= 0:
                print('Depósito inválido\n')
                tools.sleep(1)
                continue
            saldoPrev = self.saldo + deposito
            while True:
                tools.clean()
                resp = int(input('Saldo final será de R${:.2f}\n1. Confirmar\n2. Alterar depósito\n'.format(saldoPrev)))
                if 1 == resp or resp == 2:
                    break
                input("Opção inválida\nPressione enter para tentar novamente\n")
            if resp == 1:
                self.saldo = saldoPrev
            if resp == 2:
                continue
            break

    #Método que gerencia o processo de saque da conta do usuário
    def sacar(self):
        while True:
            tools.clean()
            saque = float(input('Saldo = {:.2f}\nDigite o valor a ser sacado\n'.format(self.saldo)))
            if 0 >= saque > self.saldo:
                input('Saque inválido\nPressione Enter para tentar Novamente\n')
                continue
            saldoPrev = self.saldo - saque
            while True:
                tools.clean()
                resp = int(input('Saldo final será de R${:.2f}\n1. Confirmar\n2. Alterar saque\n'.format(saldoPrev)))
                if 1 == resp or resp == 2:
                    break
                input("Opção inválida\nPressione enter para tentar novamente\n")
            if resp == 1:
                self.saldo = saldoPrev
                break
            if resp == 2:
                continue
            
