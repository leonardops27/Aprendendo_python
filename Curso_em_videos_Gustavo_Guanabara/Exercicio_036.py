print('''
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
''')
casa = float(input('Qual o valor do imóvel a comprar?: '))
salario = float(input('Qual o salário?: '))
ano_pg = int(input('Quantos anos para quitar a compra?: '))*12
valor = casa/ano_pg
limite = (salario * 30)/100
if valor <= limite:
    print('A prestação fica em R${:.2f} e 30% do seu salario são R${:.2f}. Emprestimo aprovado!'.format(valor, limite))
else:
    print('A prestação fica em R${:.2f} e 30% do seu salario são R${:.2f}. Emprestimo reprovado!'.format(valor, limite))



