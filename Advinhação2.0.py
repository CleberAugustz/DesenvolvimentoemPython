import random
import winsound
n = int(input('Advinhe o número que estou pensando!!??\nde 0 à 3\n'))
numeros = [1,2,3]
lista = random.choice(numeros)
print(lista)
if n == lista:
    print('Você acertou \o/')
while lista != n:
    print('O Número Sorteado foi {}'.format(lista))
    print('Você errou!, Tente novamentem')
    print('\033[0;31;44Caso queira sair do jogo, Digite 0')
    lista = random.choice(numeros)
    n = int(input('Advinhe o número que estou pensando!!??\nde 1 à 3\n'))
    if n == 0 :
        print('Good Bye :)')
        break
    if lista == n:
        print('\033[0;35;43mMiseravi, Acertou \o/\033[m')
        winsound.Beep(1000,500)
        winsound.PlaySound('', winsound.SND_FILENAME)
s = int(input('Digite start para jogar novamente'))