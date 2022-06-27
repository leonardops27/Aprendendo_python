print('''
Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
''')


from random import randint
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
print('''
========================================
    [1] Para 1 jogador
    [2] Para 2 jogadores
''')
jogadores = int(input('Quantos jogadores?: '))

if jogadores == 1:
    while True:
        print('''
        [0] PEDRA   
        [1] PAPEL   
        [2] TESOURA
        [3] SAIR ou outra qualquer
        ''')
        jogador = int(input('Escolha do jogador: '))
        if jogador >= 3:
            break
        computador = randint(0, 2)
        print('Vai no 3')
        sleep(1)
        print('Vai no 2')
        sleep(1)
        print('Vai no 1')
        sleep(1)
        print('Vai!!!')

        print('O computador escolheu {}.'.format(itens[computador]))
        print('Jogador escolheu {}.'.format(itens[jogador]))
        if computador == jogador:
            print('Empataram.')
        elif computador == 0:
            if jogador == 1:
                print('O Jogador venceu o computador!')
            elif jogador == 2:
                print('O Jogador perdeu para o computador.')
        elif computador == 1:
            if jogador == 0 :
                print('Jogador perdeu para  o computador.')
            elif jogador == 2 :
                print('Jogador venceu o computador!')
        elif computador == 2:
            if jogador == 0:
                print('Jogador venceu o computador!')
            elif jogador == 1:
                print('Jogador perdeu para o computador.')
elif jogadores == 2:
    print('''
    [0] PEDRA   
    [1] PAPEL   
    [2] TESOURA
     ''')
    jogador1 = int(input('Escolha do jogador 1: '))
    jogador2 = int(input('Escolha do jogador 2: '))

    computador = randint(0,2)
    print('Vai no 3')
    sleep(1)
    print('Vai no 2')
    sleep(1)
    print('Vai no 1')
    sleep(1)
    print('Vai!!!')

    print('O computador escolheu {}.'.format(itens[computador]))
    print('Jogador 1 escolheu {}.'.format(itens[jogador1]))
    print('Jogador 2 escolheu {}.'.format(itens[jogador2]))

    if computador == 0:
        if computador == jogador1 and computador == jogador2:
            print('Todos empataram !!! ')
        elif jogador2 == 0 and jogador1 == 2:
            print('Empate do Jogador 2 e o Computador, os dois vencem o Jogador 1 !!!')
        elif jogador1 == 0 and jogador2 == 2:
            print('Empate do Jogador 1 e Computador, os dois vencem o Jogador 2 !!!')
        elif jogador1 == 1 and jogador2 == 2:
            print('Jogador 1, venceu o computador e Jogador 2, venceu o Jogador 1.')
        elif jogador1 == 2 and jogador2 == 1:
            print('Jogador 2, venceu o computador e Jogador 1, venceu o Jogador 2.')

    elif computador == 1:
        if computador == jogador1 and computador == jogador2:
            print('Todos empataram !!! ')
        elif jogador1 == 0 and jogador2 == 0:
            print('Jogador 1 e 2 perderam para  o computador.')
        elif jogador1 == 0 and jogador2 == 1:
            print('O Jogador 1 ')
        elif jogador1 == 0 and jogador2 == 2:
            print('Empate do Jogador 1 e Computador. Jogador 1, venceu o Jogador 2.')
        elif jogador1 == 1 and jogador2 == 0:
            print('Empate do Jogador 1 e Computador. Jogador 1, venceu o Jogador 2.')
        elif jogador1 == 2 and jogador2 == 0:
            print('Jogador 1, venceu o computador e Jogador 2, venceu o Jogador 1.')
        elif jogador1 == 2 and jogador2 == 1:
            print('Empate do Jogador 2 e o Computador. Jogador 2, venceu o Jogador 1.')
        elif jogador1 == 0 and jogador2 == 2:
            print('Jogador 2, venceu o computador e Jogador 1, venceu o Jogador 2.')

    elif computador == 2:
        if computador == jogador1 and computador == jogador2:
            print('Todos empataram !!! ')
        elif jogador2 == 2 and jogador1 == 1:
            print('Empate do Jogador 2 e o Computador, os dois vencem o Jogador 1 !!!')
        elif jogador1 == 2 and jogador2 == 1:
            print('Empate do Jogador 1 e Computador, os dois vencem o Jogador 2 !!!')
        elif jogador1 == 0 and jogador2 == 1:
            print('Jogador 1, venceu o computador e Jogador 2, venceu o Jogador 1.')
        elif jogador1 == 1 and jogador2 == 0:
            print('Jogador 2, venceu o computador e Jogador 1, venceu o Jogador 2.')




