print('''
Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
''')
num = int(input('Digite qual tabuada quer ler: '))
for mult in range(1,11):
    tabuada = mult * num
    print('{} x {} = {}'.format(num,mult,tabuada))

