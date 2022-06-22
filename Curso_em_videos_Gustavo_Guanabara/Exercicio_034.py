print('''
Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
''')
salario = float(input('Qual o salario: '))
if salario <= 1250.00:
    print('Seu salario de R${:.2f} teve um reajuste de 15% igual a R${:.2f} e foi para R${:.2f} .'.format(salario,(salario*15)/100,salario+(salario*15)/100))
else:
    print('Seu salario de R${:.2f} teve um reajuste de 10% igual a R${:.2f} e foi para R${:.2f} .'.format(salario, (salario*10)/100,salario+(salario * 10) / 100))

