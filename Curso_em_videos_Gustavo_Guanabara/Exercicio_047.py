print('''
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
Tem 2 exemplos nesse arquivo onde 1º inicia com número "1" e vai até "51" intercalado "2" (1,51,2).
O 2º inicia com "2" e vai até o número "51" também intercalado "2" (2,21,2).
No primeiro exemplo determinamos o inicio com numero impar então temos números impares e no segundo números pares.
No exemplo, se modificar a terceira configuração (1,51,2) item "2" para "3" irá intercalar 3x3.
Observar o " print() " vazio, a função anterior " print " determina a finalização no espaço que seria a proxima linha
juntando ambas as linhas, assim após a proxima linha vazia continua normal.
''')
print('primeiro exemplo:')
for numero in range(1,51,2):
    print(numero, end= '  ')
print()
print('Segundo exemplo:')
for num in range(2,21,2):
    print(num)

