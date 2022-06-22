print('''
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
''')

escolha = 0
while escolha != 3:
    num = int(input('Digite o numero para conversão: '))
    print('''
    Escolha a conversão ou qualquer outro número para sair
    =====================================================
        [1] Binário     [2] Octal   [3] Hexadecimal
    ''')
    escolha = int(input('Digite o numero da escolha: '))
    if escolha == 1:
        print('O número {} em Binário é:{}.'.format(num, bin(num)))
    elif escolha == 2:
        print('O número {} em Octal é: {}.'.format(num, oct(num)))
    elif escolha == 3:
        print('O numero {} em Hexadecimal é: {}.'.format(num, hex(num)))
    else:
        break



