
print('''Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

Estudo de "condições"
''')
import random
comp = random.randint(0,5)
print('O Computador escolheu um número entre 0 e 5, qual numero ele escolheu?')
jogador = int(input('Qual número vai escolher?: '))
if jogador == comp:
    print('Você acertou!')
else:
    print('Você errou!')
print('O número do computador foi "{}" e o seu foi "{}".'.format(comp, jogador))