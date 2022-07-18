print('''
Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
''')

num = soma = vzs = 0

while num != 999:
    num = int(input('Digite o número [999 para sair]: '))
    if num == 999:
        break
    soma += num
    vzs += 1
print('{} valores que somam {} e média de {:.2f}'.format(vzs,soma,soma/vzs))


