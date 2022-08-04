print('''
Exercício Python 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
''')
while True:
    extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze',
               'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
    while True:
        numero = int(input('\033[39mDigite um número de 0 a 20: '))
        if 0 <= numero <= 20:
            break
        print('Tente novamente, você consegue! ', end='')
    print('Você digitou o número\033[31m',extenso[numero])
    continuar = input('\033[34mDeseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break