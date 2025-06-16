#coisas que precisam ser arrumadas:
#1. o menu precisa ser feito em um loop e o balanço da conta deve ser lembrado
#2. precisamos achar um jeito de fazer com que você possa jogar infinitamente até que um botão seja apertado. Enquanto isso, a qualquer momento você deve poder adicionar fundos
import random
from uteis import ferramentas as tools

#Função que imprime os números da roleta e suas respectivas cores
def roleta():                                        
    for x in range(37):
        if x==0:
            tools.prGreen(x)
        if x>0 and x<=10 or x>=19 and x<=28:
            if x%2==0:
               tools.prBlack(x)
            if x%2==1:
               tools.prRed(x)
        if x>10 and x<=18 or x>=29 and x<=36:
            if x%2==1:
               tools.prBlack(x)
            if x%2==0:
               tools.prRed(x)

#Retona um valor pra caso o número seja vermelho, preto ou Verde (1 = vermelho, 2 = preto, 3 = verde)
def RorBorG(x):
    if x==0:
         return 3
    if x>0 and x<=10 or x>=19 and x<=28:
        if x%2==0:
          return 2
        if x%2==1:
          return 1
    if x>10 and x<=18 or x>=29 and x<=36:
         if x%2==1:
          return 2
         if x%2==0:
          return 1
              

def jogar(user):
     tools.clean()

     aposta = -1
     apout = -1

     tools.clean()
     conta = user.saldo
     while aposta > 36 or aposta < 0:
          tools.clean()
          roleta()
          aposta = int(input('Selecione sua aposta interna: 0-36\n'))
          if aposta > 36 or aposta < 0:
               print('Valor inválido, Selecione um númeor entre 0-36')

     valor = int(input('Quanto deseja apostar?\n'))

     if valor > conta:
          print('Fundos insuficientes')
          tools.sleep(1)
          return

     conta = conta - valor

     while apout < 1 or apout > 3:
          tools.clean()
          roleta()
          apout = int(input('Selecione sua aposta externa: \n1. pretas(2x) \n2. Vermelhas(2x)\n3. Verde(20x)\n'))
     
     valout = int(input('Quanto deseja apostar?\n'))

     if valout > conta:
          print('Fundos insuficientes')
          tools.sleep(1)
          return

     conta = conta - valout
     tools.clean()

     print('seu número é :' + str(aposta))

     if apout == 1:
          print('Você apostou nas Vermelhas')
     if apout == 2:
          print('Você apostou nas Pretas')
     if apout == 3:
          print('Você apostou na Verde')

     ganhador = random.randint(0, 36)

     if apout == RorBorG(ganhador):
          if apout == 3:
               conta = conta + 20*valout
          if apout == 1 or apout == 2:
               conta = conta + 2*valout

     print('O Valor sorteado é: ' + str(ganhador))

     if RorBorG(ganhador) == 1:
          print(str(ganhador) + ' é Vermelho\n')
     if RorBorG(ganhador) == 2:
          print(str(ganhador) + ' é Preto\n')
     if RorBorG(ganhador) == 3:
          print(str(ganhador) + ' é Verde\n')


     if ganhador == aposta:
          conta = conta + 10 * valor

     input('seu novo saldo é: {}R$\nPressione enter para continuar'.format(conta))
     user.saldo = conta