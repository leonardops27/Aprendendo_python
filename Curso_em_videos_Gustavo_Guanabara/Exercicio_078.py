import random
print('''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
''')

valores = []
impar = []
par = []
maior = []
menor = []
obs1 = []


for x in range(0,5):
    #numero = int(input(f'Entre com {x+1}º valor: '))
    numero = random.randint(1,9)# usado para fazer a entrada dos números para desenvolvimento

    valores += [numero]
    if numero % 2 == 0:
        par += [numero]
    if numero % 2 == 1:
        impar += [numero]

    if numero % 2:
        obs1 += [numero]

    if numero <= 0:
        numero = menor
    else:
        maior = numero
print(f'Os valores digitados são {valores}')
print(f'número maior é {max(valores)}, menor {min(valores)}, impar {impar}, par {par}')
print(f'Observe que a saída é a mesma para impar {obs1}, codigos diferentes:')
print(f'<if numero % 2:> é saída impar {obs1}, agora <if numero % 2 == 0:> com "0" é par {par}, e "1" é impar {impar},')

lista = []
mai = []
men = []
for z in range(0,4):
    lista.append(int(input(f'Informe o valor referente posição {z}: ')))
    if z == 0:
        mai = men = lista[z]
    else:
        if lista[z] > mai:
            mai = lista[z]
        if lista[z] < men:
            men = lista[z]
print(f'Os numero são {lista}')
print(f'o maior é {mai} na posição ', end='')
for a, w in enumerate(lista):
    if w == mai:
        print(f'{a}, ', end='')
print()
print(f'O menor valor foi {men} na posição: ', end='')
for b, c in enumerate(lista):
    if c == men:
        print(f'{b}, ', end='')
print()
print('fim')


