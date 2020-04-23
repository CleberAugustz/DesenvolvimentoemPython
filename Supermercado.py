try:
    def begin():
        print('='*10,'Supermercado!!','='*10)
        valor = float(input('Digite Valor da Compra R$:\n'))
        print('Formas de pagamento')
        pag = int(input('1 - A vista Dinheiro/Cheque 10% de Desconto\n2 - Á vista no Cartão 5% de Desconto\n3 - Em até 2x no cartão, Preço normal\n4 - 3x ou mais no cartão, 20% de Juros\n'))

        if pag == 1:
            a = valor*0.90
            print('Você irá pagar R${}'.format(a))
        elif pag == 2:
            a = valor*0.95
            print('Você irá pagar R${}'.format(a))
        elif pag == 3:
            parcela = int(input('Quantas Parcelas?\n'))
            if parcela <= 2:
                print('Você irá pagar R${}'.format(valor))
            else:
                a = valor*1.20
                print('Você irá pagar R${}'.format(a))
    begin()
except:
    print('Por Favor, respeite as regras do sistema')
    print('Restartando!!')
    begin()