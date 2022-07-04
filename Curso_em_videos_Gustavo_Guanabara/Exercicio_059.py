print('''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
''')
print('\033[36m_'*5,'\033[32mEntre com os valores e escolha no menu.','\033[36m_'*5)
valor1 = int(input('Entre com o 1º valor: '))
valor2 = int(input('Entre com o 2º valor: '))
menu = 0
while menu != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do app
    ''')
    opc = int(input('Qual sua opção?: '))
    if opc == 1:
        print('A soma dos números é {}.'.format(valor1 + valor2))
    if opc == 2:
        print('A multiplicação dos valores é {}.'.format(valor1 * valor2))
    if opc == 3:
        if valor1 == valor2:
            print('Os valores são iguais.')
        if valor1 > valor2:
            print('O primeiro valor, "{}", é maior.'.format(valor1))
        if valor1 < valor2:
            print('O segundo valor, "{}", é maior.'.format(valor2))
    if opc == 4:
        valor1 = int(input('Entre com o 1º valor: '))
        valor2 = int(input('Entre com o 2º valor: '))
    if opc == 5:
        print('\n\033[36mSAIR!!! Até a proxima.')
        break







