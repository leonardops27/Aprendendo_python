print('''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
''')

num2 = ()
num3 = []
ipar = ''
parr = ''

for y in range(0,6):
    numero = int(input(f'Digite o {y+1}º número: '))
    num2 += numero,
    num3 += numero,
    if numero % 2 == 0:
        parr = numero, parr
    else:
        ipar = numero, ipar
print('Linha para testes', num2,num2[1])
print('Linha para testes',num3[3])
a = int(input('Qual número quer saber quantas vezes apareceu?: '))
b = int(input('Qual número deseja saber a posição?: '))
aa = num3.count(b)
count = ()
print('linha de este', aa, count)
for z in range(aa):
    count += (num2.index(b)),
print('vezes:',aa,' e o loop: ',count)
print(f'O número {a} apareceu {num2.count(a)} vezes.')
print(f'O número {b} está na {num2.count(b),num2.index(b)+1}º posição.')
print(f'Resultado: numero={num3}, impar={ipar}, par={parr}')

'''
num = (int(input('Digite o 1º valor: ')),
      int(input('Digite o 2º valor: ')),
      int(input('Digite o 3º valor: ')),
      int(input('Digite o 4º valor: ')))
print(f'Você digitou os números \033[34m{num},\033[39m faça sua escolha abaixo.')
a = int(input('Qual número quer saber quantas vezes apareceu?: '))
b = int(input('Qual número deseja saber a posição?: '))
print(f'O número {a} apareceu {num.count(a)} vezes.')
print(f'O número {b} está na {num.index(b)+1}º posição.')
print('Os números pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n},', end='')
'''


