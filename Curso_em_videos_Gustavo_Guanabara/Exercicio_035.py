print('''
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
''')
print('Informe todos os comprimentos em uma das medidas: metros, centímetros, etc')
c1 = float(input('Digite o primeiro comprimento: '))
c2 = float(input('Digite o segundo comprimento: '))
c3 = float(input('Digite o terceiro comprimento: '))
if c1 < c2+c3 and c2 < c1+c3 and c3 < c1+c2:
    print('Os comprimentos "{}", "{}" e "{}", formam um triângulo!'.format(c1,c2,c3))
    print('Os comprimentos "{:.0f}", "{:.0f}" e "{:.0f}", formam um triângulo!'.format(c1, c2, c3))
else:
    print('Os comprimentos "{}", "{}" e "{}", não formam um triângulo.'.format(c1,c2,c3))
    print('Os comprimentos "{:.0f}", "{:.0f}" e "{:.0f}", não formam um triângulo.'.format(c1, c2, c3))
