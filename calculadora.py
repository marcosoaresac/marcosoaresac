from time import sleep
import os

class Calculadora():

    def Soma(self,numero1,numero2):

        resultado = numero1 + numero2
        print('Resultado: ',resultado)
        sleep(2)
        os.system('cls')
        self.Menu()

    def Subtrair(self,numero1,numero2):

        resultado = numero1 - numero2
        print('Resultado: ',resultado)
        sleep(2)    
        os.system('cls')
        self.Menu()

    def Multiplicar(self,numero1,numero2):

        resultado = numero1 * numero2
        print('Resultado: ',resultado)
        sleep(2)
        os.system('cls')
        self.Menu()

    def Dividir(self,numero1,numero2):

        resultado = numero1 / numero2
        print('Resultado: ',resultado)
        sleep(2)
        os.system('cls')
        self.Menu()

    def Menu(self):
        numero1 = float(input('Digite o 1º numero: '))
        numero2 = float(input('Digite o 2º numero: '))

        print('''
        | Escolha uma Operação |
        [1] - Somar
        [2] - Subtrair
        [3] - Multiplicação
        [4] - Divisão
        [0] - Sair
        ''')
        op = int(input('> '))

        if op == 1:
            self.Soma(numero1,numero2)
        elif op == 2:
            self.Subtrair(numero1,numero2)
        elif op == 3:
            self.Multiplicar(numero1,numero2)
        elif op == 4:
            self.Dividir(numero1,numero2)
        elif op == 0:
            print('Encerrando calculadora...')
            sleep(2)
        else:
            print('Comando inválido.')
            sleep(2)
            self.Menu()
        sleep(2)
        os.system('cls')

calculadora = Calculadora()
calculadora.Menu()