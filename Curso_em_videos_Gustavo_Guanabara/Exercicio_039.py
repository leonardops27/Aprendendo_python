print('''
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
''')

from datetime import date, datetime

d_hoje = date.today()
hoje = d_hoje.strftime('%d/%m/%Y')
print('='*3,'A data de hoje é: {}.'.format(hoje))

ano_hoje = date.today().year
nasci = int(input('Qual ano de nascimento?: '))
idade = ano_hoje - nasci
print('Nascido em {} tem {} anos em {}'.format(nasci, idade, ano_hoje))

if idade == 18:
    print('Você tem que se alistar esse ano.')
elif idade < 18:
    tempo = 18 - idade
    ano = ano_hoje + tempo
    print('Faltam {} anos para seu alistamento. Seu alistamento é em {}.'.format(tempo, ano))
elif idade > 18:
    tempo = idade - 18
    ano = ano_hoje - tempo
    print('Seu alistamento foi a {} anos atrás, em {}.'.format(tempo,ano))
