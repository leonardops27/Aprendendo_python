print('''
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
''')
primeiro = int(input("Entre com o primeiro termo da PA: "))
razao = int(input("Entre com a razão da PA: "))
termo = primeiro
cont = 1
total = 0
adicao = 10
while adicao != 0:
    total = total + adicao
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('...PAUSA...')
    adicao = int(input('Quantos mais termos você que ler?: '))
print(total)


