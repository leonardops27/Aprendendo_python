print('''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 – 1 – 1 – 2 – 3 – 5 – 8
''')
num = int(input('Entre com um número: '))
fibo1 = 0
fibo2 = 1
cont = 3
while cont <= num:
    fibo3 = fibo1 + fibo2
    print('{} -> '.format(fibo3), end='')
    fibo1 = fibo2
    fibo2 = fibo3
    cont += 1
print('Fim!')

