print('''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechados na ordem correta.
''')

expre = str(input('Digite a expressão: '))
pilha = []
for simbol in expre:
    if simbol == '(':
        pilha.append('(')
    elif simbol == ')':
        if len(pilha) > 0:
            pilha.pop()#remove último elemento da lista.
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!')
    print(expre)
else:
    print('Sua expressão está errada!')

