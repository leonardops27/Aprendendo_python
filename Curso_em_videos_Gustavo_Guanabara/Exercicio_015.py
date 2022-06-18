print('''
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
''')
km = float(input('Quanto quilometros percorridos? '))
dias = int(input('Quantos dias alugado? '))
c_km = float(km*0.15)
c_dias = dias*60
total = c_km + c_dias

print('='*3,'Modo 1, aqui cria mais objetos','='*3)
print('O carro ficou alugado por {:.0f} dias e percorreu {:.0f} Km, total do aluguel é R${:.2f}. Grato!'.format(dias,km,total))
print('*'*3,'Modo 2, aqui usamos três linhas de código.(2 input + 1 print','*'*3)
print('O carro ficou alugado por {:.0f} dias e percorreu {:.0f} Km, total do aluguel é R${:.2f}. Grato!'.format(dias,km,(dias*60)+(km*0.15)))
print()
print('#'*5,'Nesse proximo exemplo obtem a entrada e o resultado em apenas uma linha de codigo','#'*5)
print((int(input('Digite o Km: '))*0.15)+(int(input('Digite os dias: '))*60))
