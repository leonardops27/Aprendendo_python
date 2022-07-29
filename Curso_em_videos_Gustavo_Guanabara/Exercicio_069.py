print('''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
''')
nome = []
sexo = masculino = feminino = fem20 = idade = mais18 = menos18 = pessoas = 0
while True:
    print('Inicio')
    nome = str(input('Digite o nome: '))
    pessoas += 1
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        mais18 += 1
    sexo = str(input('Escolha o sexo [F/M]: ')).strip().upper()
    if sexo == 'F' and idade <= 20:
        fem20 += 1
    if sexo == 'F':
        feminino += 1
    if sexo == 'M':
        masculino += 1
    continuar = str(input('Fazer novo cadastro? [S]/[N]: ')).strip().upper()
    if continuar == 'N':
        break
print('Cadastrado {} pessoas, {} Homens e {} mulheres com 20 anos menos.'.format(pessoas, masculino, fem20))