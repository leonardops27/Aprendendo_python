print('''
Exercício Python 14: Escreva um programa que converta uma temperatura digitando em
graus Celsius e converta para graus Fahrenheit.
''')
temp_c = float(input('Qual a temperatura em Celsius?: '))
temp_f = ((9*temp_c)/5)+32
print('A temperatura {}º Celsius equivale a {}º Fahrenheit'.format(temp_c,temp_f))