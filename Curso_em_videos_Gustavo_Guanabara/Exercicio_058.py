print('''
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
''')
from random import randint
computador = randint(0,10)
certo = False
tentativa = 0
print('O computador escolheu um número. Qual número ele escolheu???')
while not certo:
    jogador = int(input('Jogue o número: '))
    tentativa += 1
    if jogador == computador:
        certo = True
        print('Você venceu!')
    if jogador <= computador:
        print('Jogue mais alto...')
    if jogador >= computador:
        print('Jogue mais baixo...')
print('O computador escolheu {} e você acertou com {} tentativas.'.format(computador,tentativa))
print('Fim')


