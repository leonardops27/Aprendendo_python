print('''
Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
''')
vel = int(input('Qual a velocidade do veículo em Km: '))
if vel <= 80:
    print('Sem multa!')
else:
    print('Você foi multado em R${:.2f}. Você excedeu em "{} Km/h" dos "80 km/h" permitidos'.format((vel-80)*7, vel-80))
