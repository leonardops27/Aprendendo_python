print('''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
''')
from datetime import date
d_hoje = date.today()
hoje = d_hoje.strftime('%d/%m/%Y')
ano_hoje = date.today().year
print('='*3,'A data de hoje é: {}.'.format(hoje))
ano_nasc= int(input('Digite o ano de nascimento: '))
ano = ano_hoje - ano_nasc

if ano <= 9:
    print('Categoria MIRIM')
elif ano >= 10 and ano <= 14.1:
    print('Categoria INFANTIL')
elif ano >= 15 and ano <= 19.1:
    print('Categoria JUNIOR')
elif ano >= 20 and ano <= 25.1:
    print('Categoria SÊNIOR')
elif ano >= 26:
    print('Categoria MASTER')

