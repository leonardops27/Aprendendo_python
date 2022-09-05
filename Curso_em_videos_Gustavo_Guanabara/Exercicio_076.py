print('''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
''')
listagem = ('Lapis',22,
            'Espelho',32,
            'Caderno',35,
            'Borracha',8,
            'Mochila', 120.32)
print(f'-'*40)
print(f' '*7,'*LISTAGEM DE PRODUTOS*')
print(f'_'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f' R${listagem[pos]:>7.2f}')


