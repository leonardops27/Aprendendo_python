print('''
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros
''')

produto = 0
pagamento = 0
while pagamento != 5:
    print('''
***  Comece os cálculos, siga as instruções abaixo:  ***
    ''')
    produto = float(input('Entre com valor do produto: '))
    print('''
    [1] Dinheiro ou Cheque, 10% de desconto
    [2] Cartão Debito, 5% de desconto
    [3] Cartão até 2X, preço formal
    [4] Cartão 3X ou mais, 20% de juros
    [5] Sair
    ''')
    pagamento = int(input('Digite o número desejado no menu: '))
    if pagamento == 1:
        valor = (produto * 10)/100
        print('O produto custa r${:.2f} e o pagamento em "Dinheiro ou Cheque" com desconto de 10% igual a R${:.2f}. Valor a pagar é R${:.2f}.'.format(produto,valor,produto-valor))
        #break
    elif pagamento == 2:
        valor = (produto * 5)/100
        print('O produto custa r${:.2f} e o pagamento em "Cartão de Débito" com desconto de 5% igual a R${:.2f}. Valor a pagar é R${:.2f}.'.format(produto,valor,produto-valor))
        #break
    elif pagamento == 3:
        print('O produto custa r${:.2f} e o pagamento em "Cartão até 2X" sem desconto. Valor a pagar é R${:.2f}.'.format(produto,produto))
        #break
    elif pagamento == 4:
        valor = (produto * 20)/100
        print('O produto custa r${:.2f} e o pagamento em "Cartão 3X ou mais parcelas" com juros de 20% igual a R${:.2f}. Valor a pagar é R${:.2f}.'.format(produto,valor,produto+valor))
        #break
    elif pagamento == 5:
        print('Até a proxima vez!')
        break
    else:
        print('Tente novamente! Digite o número do menu.')


