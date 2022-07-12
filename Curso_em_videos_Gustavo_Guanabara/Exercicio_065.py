print('''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
''')
continua = 'S'
soma = quant = media = maior = menor = 0
while continua in 'sS':
    num = int(input('Digite o número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input('Deseja continuar? [S/N]: ')).upper().strip()
media = soma / quant
print('{:.2f} é a média, {} é o menor e {} é o maior número'.format(media, menor, maior))
