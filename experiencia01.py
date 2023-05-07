# conta bancária 
from time import sleep

saldo = 0

class ContaBancaria():
    
    def Saque(self):
        global saldo
        saque = 0
        saque = float(input('Digite o valor do saque: '))
        if saque < saldo:
            print('Saque de R$ {} efetuado com sucesso'.format(saque))
            saldo = saldo - saque
        else:
            print('Valor indisponível para saque.')
        sleep(1)
        Menu()
        
    def Extrato(self):
        global saldo    
        print('--- Extrato Bancário ---')
        print(' Seu saldo atual é: ',saldo)
        sleep(1)
        Menu()
        
    def Deposito(slef):
        global saldo    
        deposito = 0
        deposito = float(input('Digite o valor do Depósito: '))
        saldo = saldo + deposito
        print('Depósito efetuado com sucesso.')
        sleep(1)
        Menu()
    
def Menu():
    conta_bancaria = ContaBancaria()
    print(''' 
        --- Menu ---
        1 - Saque
        2 - Extrato
        3 - Depósito
        9 - Sair
        ''')
    op = input('Escolha uma opção... ')
    if op == '1':
        conta_bancaria.Saque()
    elif op == '2':
        conta_bancaria.Extrato()
    elif op == '3':
        conta_bancaria.Deposito()
    elif op == '9':
        print('Obrigato pela visita ! Volte sempre.')
    else:
        print('Opção Inválida')
    
Menu()