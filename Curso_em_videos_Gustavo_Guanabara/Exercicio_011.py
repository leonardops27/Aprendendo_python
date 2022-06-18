print('''
Exercício Python 11: Faça um programa que leia a largura e
a altura de uma parede em metros, calcule a sua área e
a quantidade de tinta necessária para pintá-la, sabendo 
que cada litro de tinta pinta uma área de 2 metros quadrados.
''')
largura = float(input('Largura da parede? '))
altura = float(input('Altura da parede: '))
print('A parede tem {}m² e vai precisar de {:.2f} litros de tinta'.format(largura * altura, (largura * altura)/2))

