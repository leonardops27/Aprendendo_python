print('''

Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e
do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
''')
print('='*3,'Achando a Hipotenusa')
c_o = float(input('Medida do cateto oposto: '))
c_a = float(input('Medida do cateto adjacente: '))
hipo = (((c_o ** 2) + (c_a ** 2)) ** (1/2))
print('A hipotenusa dos catetos é {:.2f}'.format(hipo))

