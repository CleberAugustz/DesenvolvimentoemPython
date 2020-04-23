import time
try:
    def begin():
        n1 = int(input('Primeiro numero:\n'))
        n2 = int(input('Segundo número:\n'))
        def comparando():
            if n1 > n2:
                print('{} é maior que {}'.format(n1,n2))
            elif n2 > n1:
                print('{} é maior que {}'.format(n2,n1))
            elif n1 == n2:
                print('Não há maior, os dois são iguais')
        comparando()
    begin()
except:
    print('Houve algum erro, tente novamente!!')
    print('Reiniciando ..')
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    print('='*25)
    begin()
