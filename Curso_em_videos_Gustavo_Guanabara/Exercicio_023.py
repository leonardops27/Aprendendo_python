print('''
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.
########################################################
Considerando como base os códigos abaixo:
exemplo = num // 1000 % 10

podemos alterar seus valores:
exemplo = num // 1 % 100

Código da última sequência da análise:
a2 = num // 1 % 10 , num // 10 % 1, num // 1000 % 1000
b2 = num // 10 % 10 , num // 10 % 10 , num // 1 % 1
c2 = num // 100 % 10 , num // 10 % 100 , num // 100 % 100
d2 = num // 1000 % 10 , num // 10 % 1000 , num // 10 % 10
''')

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

a1 = num // 1 % 1
b1 = num // 1 % 10
c1 = num // 1 % 100
d1 = num // 1 % 1000

a2 = num // 1 % 10 , num // 10 % 1, num // 1000 % 1000
b2 = num // 10 % 10 , num // 10 % 10 , num // 1 % 1
c2 = num // 100 % 10 , num // 10 % 100 , num // 100 % 100
d2 = num // 1000 % 10 , num // 10 % 1000 , num // 10 % 10

print('Analisando o número {}.'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

print('Analisando o número {}, resultados quando escritos inverso.'.format(num))
print('Unidade: {}'.format(a1))
print('Dezena: {}'.format(b1))
print('Centena: {}'.format(c1))
print('Milhar: {}'.format(d1))

print('Analisando o número {} outras sequências'.format(num))
print('Unidade: {}'.format(a2))
print('Dezena: {}'.format(b2))
print('Centena: {}'.format(c2))
print('Milhar: {}'.format(d2))


