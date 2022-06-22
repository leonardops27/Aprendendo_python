print('''
Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
R$0,45 parta viagens mais longas.
''')
distancia = int(input('Qual a distancia da viagem em Km?: '))
if distancia <= 200:
    print('A distancia informada foi {} Km. Você pagará R$0,50 por Km, no total de R$ {}'.format(distancia,distancia*0.50))
else:
    print('A distancia informada foi {} Km. Você pagará R$0,45 por Km, no total de R$ {}'.format(distancia, distancia * 0.45))
