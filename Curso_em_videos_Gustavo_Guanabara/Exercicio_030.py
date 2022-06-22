print('''
Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela
se ele é PAR ou ÍMPAR.
''')
num = int(input('Digite o numero: '))
if num == 0:
    print('"0" (zero) é neutro mas pode ser considerado com número "PAR".')
elif num % 2 == False:
    print('Esse numero é "PAR".')
else:
    print('Esse numero é "ÍMPAR".')
