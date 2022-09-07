print('''
Exercício Python 4: Faça um programa que leia algo pelo teclado e 
mostre na tela o seu tipo primitivo e
todas as informações possíveis sobre ele.
''')

algo = input('Digite algo: ') # aqui é a entrada do valor que desejar

print('O tipo primitivo desse valor é',type(algo))# tudo dentro do parenteses do print() é impresso.
print('Somente espaços?', algo.isspace()) # mesma situação acima.
print('Letra ou número?', algo.isalnum()) # e assim por diante
print('É um número?', algo.isnumeric())
print('É letra?', algo.isalpha())
print('É tabela ASCII ?', algo.isascii())
print('Pode ser impresso?', algo.isprintable())
print('É um digito?', algo.isdigit())
print('Tem espaço?', algo.isspace())
print('É um identificador válido?', algo.isidentifier())
print()

while True:
    print('O digitado é um identificador válido para uma variável, apenas espaço?' )
    print('Você digitou ', algo)
    if algo.isidentifier() == True:
        print('Positivo. É um identificador válido')
    else:
        print('Negativo. Não é um identificador válido')
    if algo.isspace() == True:
        print('Positivo, somente espaços')
    else:
        print('Negativo, não é somente espaços')
    break
    
