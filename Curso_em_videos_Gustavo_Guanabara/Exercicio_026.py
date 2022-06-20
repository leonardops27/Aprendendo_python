print('''
Exercício Python 26: Faça um programa que leia uma frase pelo teclado e
mostre quantas vezes aparece a letra “A”, em que posição ela aparece a
primeira vez e em que posição ela aparece a última vez.
''')

frase = str(input('Digite uma frase: ')).upper().strip()
letra = str(input('Escolha a letra: ')).upper().strip()
print('A letra "{}" aparece {} vezes na frase.'.format(letra, frase.count(letra)))
print('A primeira letra "{}" apareceu na posição {}'.format(letra, frase.find(letra)+1))
print('A última letra "{}" apareceu na posição {}'.format(letra, frase.rfind(letra)+1))

