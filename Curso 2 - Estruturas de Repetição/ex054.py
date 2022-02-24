#Exercício 54

#Crie uma tupla preenchida com os 20 primeiros colocados do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    # apenas os 5 primeiros colocados;
    # os últimos 4 colocados da tabela;
    # uma lista com os times em ordem alfabética;
    # em que posição está o time da Chapecoense.

print('| TUPLAS COM TIMES DE FUTEBOL |')
print()

times = ('Atlético/MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fluminense', 'América/MG', 'Atlético/GO', 'Santos',
         'Ceará', 'Internacional', 'São Paulo', 'Athletico/PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')


print('Times do Brasileirão 2021: ')
print(times)
print()
print('Os 5 primeiros colocados: ')
print(times[0:5])
print()
print('Últimos 4 colocados: ')
print(times[-4:])
print()
print('Times em ordem alfabética: ')
print(sorted(times))
print()
print('O time Chapecoense está {}ª posição.'.format(times.index('Chapecoense')+1))







