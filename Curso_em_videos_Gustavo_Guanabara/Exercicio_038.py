print('''
Exercício Python 038: Escreva um programa que leia dois números inteiros e
compare-os mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
''')
num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

if num1 > num2 :
    print('O primeiro valor "{}" é maior e o segundo valor "{}" é o menor!'.format(num1, num2))
elif num1 < num2 :
    print('O segundo valor "{}" é maior e o primeiro valor "{}" é o menor!'.format(num2, num1))
else:
    print('O primeiro valor {} e segundo valor {}, são iguais!'.format(num1,num2))


