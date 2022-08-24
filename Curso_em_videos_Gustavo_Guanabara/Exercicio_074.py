print('''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
''')
from random import randint

print('Código 01:')
vezes = int(input('Quantos números quer ver: '))
maior = int(input('Apartir de qual número quer ver?: ')) # controle de maior > que.
menor = int(input('Até qual número quer ver?: ')) # controle de menor < que.
faixa_menor = maior
faixa_maior = menor
for x in range (0,vezes): # aqui escolhe quanto números quer visualizar
    n1 = randint(faixa_menor,faixa_maior) # faixa dos números a serem gerados
    n = n1
    if n1 > maior:
        maior = n1
    if n1 < menor and n1 > 0:
        menor = n1
    print(f'\033[31m{n1}',end=' ')
print(f'\033[39mSão os números gerados, \033[31m{maior} \033[39mé o maior e \033[31m{menor} \033[39mé o menor.\n')

print('Código 02:')
numeros = randint(1,10), randint(1,10), randint(1,10), randint (1,10), randint (1,10)
print(f'\033[31m{numeros} \033[39mNúmeros gerados, \033[31m{max(numeros)} \033[39mé o maior e '
      f'\033[31m{min(numeros)} \033[39mé o menor.')
