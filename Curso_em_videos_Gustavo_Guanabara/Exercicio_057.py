print('''
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
''')
sexo = str(input('Qual seu sexo? "M" masculino ou "F" feminino: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Opção invalida! Escolha "M" masculino ou "F" feminino: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
    print('\033[36m', end='')
elif sexo == 'F':
    sexo = 'Feminino'
    print('\033[35m', end='')
print('Sexo "{}" registrado.'.format(sexo))