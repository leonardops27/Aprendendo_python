print('''
Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
''')
from datetime import date
date = date.today().year
maior = 0
menor = 0
anos_maiores = []
anos_menores = []
for pessoa in range(1,8):
    ano = int(input('Digite o {}º ano: '.format(pessoa)))
    idade = (date - ano)
    if idade <= 17:
        #print('Menor idade.')
        menor += 1
        anos_menores += [ano]
    else:
        #print('Maior idade.')
        maior += 1
        anos_maiores += [ano]
print('Temos {} pessoas maiores dos anos {}.'.format(maior,anos_maiores))
print('Temos {} pessoas maiores dos anos {}.'.format(menor,anos_menores))

