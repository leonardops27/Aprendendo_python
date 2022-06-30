print('''
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão.
''')

numero = int(input('Digite o número para progressão aritmética ou tabuada: '))
razao = int(input('Digite a razão da progressão ou repita o numero anterior para tabuada: '))
contagem = 0
resultado = numero + (int(input('Quantidade de resuldados: '))) * razao
for progressao in range(numero,resultado,razao):
    contagem += 1
    print('Progressão: posição {}, numero {} e razão {} resultado {}'.format(contagem,numero, razao, progressao))
    print('Tabuada: {} x {} = {}'.format(numero,contagem,progressao))
print('''
Assim como na progressão aritmética, podemos fazer o mesmo para tabuada.
''')

