
print('''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
''')
print('*'*5,'Código do aluno', '*'*5)
lista = []
while True:
    numero = int(input('Informe o número.["0" Sair]: '))
    if numero == 0:
        lista.sort()
        print(f'Você digitou os valores {lista}')
        print('Até a proxima!')
        break
    for x in range(1):
        if numero in lista:
            print(f'O número {numero} ja existe e não será adicionado!')
            continue
        else:
            lista.append(numero)
print()
print('*'*5,'Código da aula', '*'*5)
numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')



