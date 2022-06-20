from random import random

print('''
Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

análise de string
Fatiando e escolhendo a fatia
''')
a_nome = str(input('nome = Digite o nome completo: ')).strip()# ".strip" elimina os espaços antes e depois da frase
b_nome = a_nome.split() # .split() fatia por espaços rodent de uma frase.

print('Aqui nome normal: ', a_nome)
print('Aqui nome fatiado: ', b_nome)
print('Aqui escolhido a posição [1]: ',b_nome[1])
print('Pode trocar as fatias:', b_nome[2], b_nome[1])

