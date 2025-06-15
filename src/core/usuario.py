from os import system,name
import time
def clean():                 
	if name == 'nt':           
		_ = system('cls')       
	else:                       
		_ = system('clear')
          
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
            clean()
            deposito = float(input('Digite o valor que deseja depositar:\n'))
            if deposito <= 0:
                print('Depósito inválido\n')
                time.sleep(1.5)
                continue
            saldoPrev = self.saldo + deposito
            resp = int(input('Saldo final será de {:.2f}R$\n1. Confirmar\n2. Alterar depósito\n'.format(saldoPrev)))
            while resp != 1 and resp != 2:
                resp = int(input('Número inválido digite novamente\nSaldo final será de {:.2f}R$\n1. Confirmar\n2. Alterar depósito\n').format(saldoPrev))
                time.sleep(1.5)
            if resp == 1:
                self.saldo = saldoPrev
            if resp == 2:
                continue
            break

    def sacar(self):
        while True:
            clean()
            saque = float(input('Saldo = {:.2f}\nDigite o valor a ser sacado\n'.format(self.saldo)))
            if 0 >= saque > self.saldo:
                print('saque inválido\n')
                time.sleep(1.5)
                continue
            saldoPrev = self.saldo - saque
            resp = int(input('Saldo Final: {}\n1. Confirmar\n2. Alterar Valor\n'.format(saldoPrev)))
            if resp == 1:
                self.saldo = saldoPrev
                break
            if resp == 2:
                continue
