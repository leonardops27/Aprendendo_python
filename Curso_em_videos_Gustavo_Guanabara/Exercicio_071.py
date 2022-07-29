print('''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e
o programa vai informar quantas cédulas de cada valor serão entregues. 
OBS.: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
''')
print('='*24)
print('\033[35m='*4,'\033[36m BANCO PYTHON ','\033[35m='*4)
print('\033[39m='*24)
print('''  [1]     [2]     [3]
  [4]     [5]     [6]
  [7]     [8]     [9]
          [0]''')
saque = int(input('Valor do saque R$: '))
print('='*24)
total = saque
notas = 100
tnotas = 0
while True:
    if total >= notas:
        total -= notas
        tnotas += 1
    else:
        if tnotas > 0:
            print(f'\033[31mSerão {tnotas} notas de R$ {notas}')
        if notas == 100:
            notas = 50
        elif notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        tnotas = 0
        if total == 0:
            break

print(f'\n\033[32mSalve nosso planeta!!!\nDoe agora, por favor!\n'
      'Plante as sementes das frutas que come, elas florecem arvores alimentos para nosso planeta e seres que aqui vivem.\n\n'
      f'\033[31mRetire o dinheiro R${saque:.2f}.\n\033[35mTenha um bom dia!')

