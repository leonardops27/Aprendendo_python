print('''
Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se
ela começa ou não com o nome “SANTO”.
''')
cidade = str(input('Cidade para teste: ')).strip()
teste = cidade[:5].upper() == 'SANTO'
if teste == True:
    print('O teste resultou em "{}". Sim, começa com a palavra "SANTO".'.format(teste))
else:
    print('O teste resultou em "{}". Não começa a palavra "SANTO".'.format(teste))





