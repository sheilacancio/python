print('Exercício 23')

#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO".

cidade = str(input('Nome da cidade: ')).strip()

print(cidade[:5].upper() == 'SANTO')
