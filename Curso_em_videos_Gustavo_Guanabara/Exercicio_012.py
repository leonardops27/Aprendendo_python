print('''
Exercício Python 12: Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.
''')
produto = float(input('Qual o valor do produto? '))
print('Seu produto de R${:.2f} reberá 5% de descontos. Você pagará apenas {:.2f}'.format(produto,produto-((produto*5)/100)))

