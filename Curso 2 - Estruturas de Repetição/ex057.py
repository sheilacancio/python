#Exercício 57

#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, de forma sequencial.
    #No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('| LISTA DE PREÇOS COM TUPLA |')
print()
lista = ('Caderno', 25.99,
         'Pasta', 8.90,
         'Estojo', 15.50,
         'Conjunto de lápis', 26.50,
         'Caneta (unidade)', 2.50,
         'Marcador (unidade)', 4.99)

print('-' * 40)
print('         PAPELARIA DA SHESHE       ')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>6.2f}')
