print('''
Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias,
um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos
(exceto anos múltiplos de 100 que não são múltiplos de 400). 
''')
ano = int(input('Digite o ano para saber se é ou não Bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O anos {} é "Bissexto".'.format(ano))
else:
    print('O ano {} não é "Bissexto".'.format(ano))
