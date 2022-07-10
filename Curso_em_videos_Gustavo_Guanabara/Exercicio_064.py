print('''
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
''')
vezes = 0
soma = 0
for x in range(0,999):
    num = int(input('digite o número: '))
    if num == 999:
        break
    vezes += 1
    soma += num
print('Foram digitados {} números e somam {} .'.format(vezes, soma))
print('''
num = cont = soma = 0
num = int(input('digite o número: '))
while num != 999:
    soma += num
    vezes += 1
    num = int(input('digite o número: '))
print('Foram digitados {} números e somam {} .'.format(vezes, soma))
''')