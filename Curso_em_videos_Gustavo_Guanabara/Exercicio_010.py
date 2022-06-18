print('''
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar.
''')

money = float(input('Quanto em você tem?R$  '))
cambio = float(input('Insira a taxa do câmbio USD: '))
print('Você tem R$ {} e pode comprar USD {}'.format(money, money / cambio))


