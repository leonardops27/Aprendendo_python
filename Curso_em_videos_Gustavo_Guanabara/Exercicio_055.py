print('''
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
''')

maior_peso = []
menor_peso = []
for balanca in range(1,6):
    peso = float(input('Digite o peso da {} pessoa. Kg: '.format(balanca)))
    if balanca == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso <= menor_peso:
            menor_peso = peso
print('O maior peso é {}Kg e o menor peso é {}Kg'.format(maior_peso,menor_peso))


