print('Exercício 31')

#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

print('Ano Bissexto')

ano = int(input('Digite o ano que deseja analisar: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano de {} é bissexto, pois tem 366 dias!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))

