print('''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
''')
while True:
    print('*'*15,'='*15,'*'*15)
    tabuada = int(input('\033[31mQual a tabuada? [0 para sair]: '))
    print('=' * 15)
    if tabuada <= 0:
        break
    for tabela in range(1,11):
        resposta = tabuada * tabela
        print('\033[32m{} X {} = {}'.format(tabuada,tabela,resposta))
    print()
