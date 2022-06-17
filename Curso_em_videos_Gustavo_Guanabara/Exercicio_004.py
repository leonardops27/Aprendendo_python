
algo = input('Digite algo: ')

print('O tipo primitivo desse valor é',type(algo))
print('Somente espaços?', algo.isspace())
print('Letra ou número?', algo.isalnum())
print('É um número?', algo.isnumeric())
print('É letra?', algo.isalpha())
print('É tabela ASCII ?', algo.isascii())
print('Pode ser impresso?', algo.isprintable())
print('É um digito?', algo.isdigit())
print('Tem espaço?', algo.isspace())
print('É um identificador válido?', algo.isidentifier())

print('''
while True:
    print(algo)
    if algo.isidentifier() == True:
        print('Positivo. É um identificador válido')
    else:
        print('Negativo. Não é um identificador válido')
    if algo.isspace() == True:
        print('Positivo, somente espaços')
    else:
        print('Negativo, não é somente espaços')
    break
    
''')
