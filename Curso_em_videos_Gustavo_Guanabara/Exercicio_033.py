print('''
Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
''')
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
menor = num1
maior = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('O menor numero é o {} e o maior é o {}.'.format(menor, maior))

