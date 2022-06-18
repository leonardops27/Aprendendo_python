print('''
Exercício Python 18: Faça um programa que leia um ângulo qualquer e
mostre na tela o valor do seno, cosseno e tangente desse ângulo.
''')
import math
angulo = float(input('Qual o ângulo? '))
seno = math.sin(math.radians(angulo))
print('O ângulo de {} em o Seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))
