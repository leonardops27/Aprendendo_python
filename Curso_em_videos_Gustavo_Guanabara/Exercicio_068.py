print('''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
''')
from random import randint
vezes = 0
while True:
    jogador = int(input('Escolha um número de 0 a 9 : '))
    aposta = str(input('Escolha [P] Par ou [I] Impar: ')).strip().upper()
    computador = randint(0,9)
    resultado = jogador + computador
    if resultado %2 == 0 and aposta == 'P':
        print ('{} é número "PAR". Você venceu!'.format(resultado))
        vezes += 1
    elif resultado %2 == 1 and aposta == 'I':
        print ('{} é número "IMPAR". Você venceu!'.format(resultado))
        vezes += 1
    elif resultado %2 == 0 and aposta != 'P':
        print ('Perdeu. {} é número Par. Você venceu {} vezes!!!'.format(resultado, vezes))
        break
    elif resultado %2 == 1 and aposta != 'I':
        print ('Perdeu. {} é número impar. Você venceu {} vezes!!!'.format(resultado, vezes))
        break
print('Até a proxima!')
