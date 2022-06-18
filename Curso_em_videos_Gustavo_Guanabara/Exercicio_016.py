print('''Exercício Python 16: Crie um programa que leia um número Real qualquer 
pelo teclado e mostre na tela a sua porção Inteira.
''')
import math
num = float(input('Digite um valor: '))
print('='*3,'Aqui o metodo 1, importando math e usando trunc','='*3)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
print('='*3,'Aqui o metodo 2, usa o int para apresentar o numero inteiro','='*3)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

