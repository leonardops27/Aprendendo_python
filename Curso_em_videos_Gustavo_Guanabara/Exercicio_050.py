print('''
Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma 
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
Nesse podemos saber quantos numeros ao todo, impares e pares foram digitados,
também podemos ver a soma desses números.
''')

par = 0
impar = 0
conta_par = 0
conta_impar = 0
soma_geral = 0
soma_par = 0
soma_impar = 0

for x in range(1,7):
    valor = int(input('Digite o {}º valor: '.format(x)))
    if valor % 2 == 0:
        soma_par += valor
        conta_par += 1
    elif valor % 1 == 0:
        soma_impar += valor
        conta_impar += 1

    soma_geral += valor

print('Foram {} vezes e o total dos números é {}.'.format(x, soma_geral))
print('Foram {} Pares e somam {}.'.format(conta_par, soma_par))
print('Foram {} Impares e somam {}.'.format(conta_impar, soma_impar))



