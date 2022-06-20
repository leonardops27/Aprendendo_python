print('''
Exercício Python 25: Crie um programa que leia o nome de uma pessoa e
diga se ela tem “SILVA” no nome.
''')
nome = str(input('Nome para análise: ')).strip()
print(''' observar abaixo que ocorre erro se mudar o nome para minusculo ou trocando 
.upper() x .lower() , é regra que upper é com maiusculo e lower é para minusculo.''')
analise = 'SILVA' in nome.upper()
if analise == True:
    print('A analise resultou em "{}". Sim, tem "SILVA" no nome.'.format(analise))
else:
    print('A analise resultou em "{}". Não tem "SILVA" no nome.'.format(analise))


