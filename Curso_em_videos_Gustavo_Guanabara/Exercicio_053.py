print('''
Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
''')
frase = str(input('Digite a frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso1 = ''
inverso2 = junto[::-1]
for letra in range(len(junto)-1,-1,-1):
    print(junto[letra])
    inverso1 += junto[letra]
if junto == inverso1:
    print('Você digitou um "palíndromo"!')
else:
    print('O digitado não é um "palíndromo".')
print('Método 1 - Esse é o normal sem espaços {} e esse o invertido {}'.format(junto,inverso1))
print('Método 2 - Esse é o normal sem espaços {} e esse o invertido {}, nesse eliminamos o "for".'.format(junto,inverso2))
#print('A frase é: {}'. format(frase))
#print('A frase é: {}'. format(palavra))
#print('A frase é: {}'. format(junto))

