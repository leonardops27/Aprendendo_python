print('''
Exercício Python 8: Escreva um programa que leia um valor em metros e
o exiba convertido em centímetros e milímetros.
''')
medida = float(input('Medida em métro: '))
print('{} metros tem {} Decimetros, {} Centimetros e {} Milimetros'.format(medida, medida*10, medida*100, medida*1000))
print('{} metros tem {} Decametros, {} Hectometros e {} Quilometros'.format(medida, medida/10, medida/100, medida/1000))

