print('''
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
''')
numero = int(input('Entre com o numero: '))
total = 0
for contagem in range(1,numero + 1):
    if numero % contagem == 0:
        #print(numero)
        print('\033[33m', end='')
        total += 1
    else:
        #print(numero)
        print('\033[34m', end='')
    print('{} '.format(contagem), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(numero,total))
if total == 2:
    print('Sim, número primo.')
else:
    print('Não é número primo.')



