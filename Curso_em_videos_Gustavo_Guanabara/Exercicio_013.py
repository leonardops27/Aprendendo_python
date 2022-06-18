print('''
Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.
''')
print('*'*3,'Digite somente numeros','*'*3)
salario = int(input('Qual o salario?: '))
aumento = int(input('Qual percentual do aumento?: '))
print('Seu salário de R${:.2f} teve um reajuste de {}% que equivale a R${:.2f}. Novo salario é R${:.2f}'.format(salario,aumento,salario*aumento/100,salario+salario*aumento/100))

