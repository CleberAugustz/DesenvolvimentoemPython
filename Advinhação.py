import random
import time
jogador = int(input('Adivinhe o número que estou pensando. 0 a 5\n'))
###lista = (1,2,3,4,5)
###n = random.choice(lista)
computador = random.randint(0, 5)
print('-=-' * 15)
print('Hmmmm.... eu acho que você')
print('-=-' * 15)
print('Processando.....')
time.sleep(5)
print('O número sortiado é {}'.format(computador))
if jogador == computador:
    print('Você acertou...  ¬¬')
else:
    print('Você errou, eu ganhei HAHAHA')
