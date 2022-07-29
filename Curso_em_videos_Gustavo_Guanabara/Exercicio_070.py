print('''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
''')
total = mil = menorv = cont = 0
barato = ''
while True:
    print('='*5,'Cadastro de produto','='*5)
    produto = str(input('Qual o produto?: ')).strip().upper()
    valor = int(input('Qual valor?: '))
    cont += 1
    if valor >= 1000:
        mil += 1
    if valor < menorv or cont == 1:
        menorv = valor
        barato = produto
    total += valor
    sair = str(input('Continuar? [S/N]: ')).strip().upper()
    if sair == 'N':
        break

print('Total é R${:.2f}, {} produto(s) mais de R$1000.00 \ne {} é o produto mais batato com custo de R${:.2f}.'.format(total, mil, barato, menorv))

