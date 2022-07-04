print('''
Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e
quantas mulheres têm menos de 20 anos.
''')
somaidade = 0
mediaidade = 0
maioridhomem = 0
maioridmulher = 0
nomeh = ''
nomem = ''
totalh20 = 0
totalm20 = 0

for pessoa in range(1,5):
    print('-'*5,'{}º PESSOA'.format(pessoa),'-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    somaidade += idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if pessoa == 1 and sexo in 'M':
        maioridhomem = idade
        nomeh = nome
    if pessoa == 1 and sexo in 'F':
        maioridmulher = idade
        nomem = nome
    if sexo in 'M' and idade > maioridhomem:
        maioridhomem = idade
        nomeh = nome
    if sexo in 'F' and idade > maioridmulher:
        maioridmulher = idade
        nomem = nome
    if sexo in 'F' and idade < 20:
        totalm20 += 1
    if sexo in 'M' and idade < 20:
        totalh20 += 1
#mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos.'.format(somaidade/pessoa))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridhomem,nomeh))
print('A mulher mais velha tem {} anos e se chama {}.'.format(maioridmulher,nomem))
print('Ao todo tem {} homens com menos de 20 anos'.format(totalh20))
print('Ao todo tem {} mulheres com menos de 20 anos'.format(totalm20))
