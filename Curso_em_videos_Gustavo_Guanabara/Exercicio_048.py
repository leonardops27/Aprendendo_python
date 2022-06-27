print('''
Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
que se encontram no intervalo de 1 até 500.
Esse exercicio é parecido com anterior, porém o controle fica na proxima linha, criado uma condição.
''')
soma = 0
contagem = 0
for num in range(1,501,2):
    if num % 3 == 0:
        contagem = contagem + 1
        soma = soma + num
print('Quantidade de valores a ser somados divisiveis por 3 são :{} e tem o resultado de :{}.'.format(contagem,soma))

print()
for num1 in range(1,20):
    if num1 % 3 == 0:
        print(num1, end=' ')
print()
for num2 in range(1,20):
    if num2 % 2 == 0:
        print(num2)



