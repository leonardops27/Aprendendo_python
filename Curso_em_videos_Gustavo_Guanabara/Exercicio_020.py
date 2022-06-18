print('''
Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de
trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
''')
import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
lista = [n1, n2, n3, n4]
print('--- Primeiro Exemplo ---')
for xx in lista:
    print(xx)
random.shuffle(lista)
print('--- Segundo Exemplo ( Observar a diferença antes e depois do "random.shuffle(lista) ---')
print('A ordem de apresentação será primeiro {}'.format(lista))
print()
print('--- Terceiro exemplo ---')
print(lista)
print()
print('--- Quarto exemplo ---')
for x in lista:
    print(x)
