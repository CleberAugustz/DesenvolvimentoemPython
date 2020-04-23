ano = int(input('Digite seu ano de nascimento:\n'))
idade = 2020 - ano
if idade == 18:
    print('Quem nasceu em {} fez {} anos em 2020'.format(ano,idade))
    print('Se aliste imediatamente!!')
elif idade < 17:
    print('Quem nasceu em {} fez {} anos em 2020.'.format(ano,idade))
    a = 18 - idade
    print('Ainda faltam {} anos para você se alistar.'.format(a))
    print('Seu Alistamento será em {}.'.format(2020+a))
elif idade >= 19:
    print('Quem nasceu em {} fez {} anos em 2018'.format(ano,idade))
    a = idade - 18
    print('Seu alistamenteo foi em {}.'.format(2020-a))


