import math
import time

while True:
    print('\033[1;4;30m-=-' * 30)
    var = input('''\033[0;37mEscolha qual tipo de conta você quer fazer 
    ou se desejar achar a raiz quadrada ou cubica digite (raiz2) ou (raiz3): ''')
    n1 = float(input('\033[0;37mEscolha um numero para calcular: '))
    n2 = float(input('\033[0;37mEscolha outro numero para calcular: '))
    cub = math.ceil(n1)
    if var == ('+'):
        print('\033[1;4;37mResultado\033[0;34m \033[0;35m{} + {} = {}' .format(n1, n2, n1+n2))
    elif var == ('-'):
        print('\033[1;4;37mResultado\033[0;34m \033[0;36m{} - {} = {}' .format(n1, n2, n1-n2))
    elif var == ('*'):
        for t in range(1,11):
            print(f'\033[1;4;37mTabuada\033[m\033[1;37m -> {n1:0} x {t:0} = {n1*t:0}')
        print('\033[1;4;37mResultado\033[0;34m \033[0;34m{} * {} = {}' .format(n1, n2, n1*n2))
    elif var == ('/'):
        print('\033[1;4;37mResultado\033[0;34m \033[0;32m{} / {} = {}' .format (n1, n2, n1/n2))
    elif var == ('raiz2'):
        print ('\033[1;4;37mResultado\033[0;34m \033[1;30m{}\033[0m tem sua raiz quadrada como \033[1;30m{:.2f}' .format(n1, cub**(1/2)))
    elif var == ('raiz3'):
        print('\033[1;4;37mResultado\033[0;34m \033[0;31m{}\033[0m tem sua raiz cubica como \033[0;31m{:.2f}' .format(n1, cub**(1/3)))
    elif var == ('%'):
        print('\033[1;4;37mResultado\033[0;34m \033[0;33m{}%\033[0m de \033[0;33m{}\033[0m é \033[0;33m{}' .format(n2, n1, n1*n2/100))
    else:
        print('\033[1;4;31mErro comando invalido!!\033[0m')
    print('\033[1;4;30m-=-' * 30)
    resp = str(input('\033[1;4;mDeseja fazer outra conta? [S/N] ')).upper().strip()[0]
    if resp != 'S':
        print('\033[1;4;31mEncerrando programa...')
        time.sleep(0.4)
        print('\033[1;4;31mPrograma encerrado!!!')
        break
print('\033[1;4;30m-=-' * 30)
