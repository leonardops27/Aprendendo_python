print('''\033[33m
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da 
Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
''')

times = ('Flamengo','Fluminense','Vasco','Botafogo','Chapecoense','Cruzeiro','Corinthias','Coritiba','Goias','Santos',
         'Palmeiras','Juventude','Cuiabá','Fortaleza','Avaí','Internacional','Bragantino','Atl.Minas','America','Brasiliense')
print(f'\033[39mOs 4 primeiros são:\033[36m{times[0:4]}\n\033[39mOs 4 ultimos são:\033[31m{times[16:20]}')
print(f'\033[39mOs times em ordem alfabética.\033[32m{sorted(times)}')
print(f'\033[36mO time \033[33m{times[5-1]} \033[36mestá na \033[33m{times.index("Chapecoense")+1}º\033[36m colocação.')
