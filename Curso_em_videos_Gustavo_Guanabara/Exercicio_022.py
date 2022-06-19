print('''
Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
''')
nome = str(input('Qual seu nome completo? '))
print('Olá {}! Veja abaixo alguns dados do seu nome.'.format(nome.upper()))
print('{}, veja seu nome em maiúsculo: {}'.format(nome, nome.upper()))
print('Agora {}, seu nome em minúsculo: {}.'.format(nome,nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print(' outras formas {}'.format(nome))
separar = nome.split()
print(separar)

