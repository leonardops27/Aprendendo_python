import random

print('''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.
''')

lista = []
for c in range(0,5):
    n= int(input(f'Digite o {c+1}º valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')



'''
numeros = []
ordem = [0]
ponto = [0]
while True:
    for x in range(1,6):
        #num = int(input(f'Digite o {x}º número: '))
        num = random.randint(1,9)
        numeros += [num]

    for z in range(len(numeros)):
        print(numeros)


print(ordem)






print()
print('='*5,'Código da aula','='*5)
lista = []
for c in range(0,5):
    n = int(input(f'Digite o {c+1}º número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista numérica.')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')

'''