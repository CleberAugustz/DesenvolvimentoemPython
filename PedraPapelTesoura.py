#coding: utf-8

__author__ = 'Cleber Augusto Dias Da Silva'

########################
#### Cleber Augusto ####
########################

import random
import time
class jogo:
    a = 0
    l = []
    l2 = []
    b = 0
    def __init__(self):
        print('Suas opções:\n')
        self.a = int(input('0 - PEDRA\n1 - PAPEL\n2 - TESOURA\nQual é a sua jogada?\n'))
        self.l = [0, 1, 2]
        self.l2 = ["Pedra", "Papel", "Tesoura"]
        self.b = random.choice(self.l)
        print('JO')
        time.sleep(1)
        print('KEN')
        time.sleep(1)
        print('PO!!!')
        print('-='*15)
        print('Computador Jogou {}'.format(self.l2[self.b]))
        print('Jogador jogou {}'.format(self.l2[self.a]))
        print('-='*15)
        if self.a == 0 and self.b == 1:
                print('O ganhador é o Computador')
        elif self.a == 1 and self.b == 2:
                print('O ganhador é o Computador')
        elif self.a == 0 and self.b == 2:
                print('O ganhador é o Computador')
        elif self.a == self.b:
                print('Não houve ganhadores.\nHá um empate!')
        else:
                print('O ganhador é o jogador')
jg = jogo()
