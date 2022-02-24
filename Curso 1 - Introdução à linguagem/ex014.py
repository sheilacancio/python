print('Exercício 14')

#Faça um algoritmo que leia o preço de um produto e mostre seu novo valor com 5% de desconto.

print('PROMOÇÃO DOS 5% DE DESCONTO')

preco = float(input('Valor do produto para compra: R$ '))
descontar = preco * 5 / 100
desconto = preco - descontar
print('O produto que antes custava R${:.2f}, na promoção com desconto de 5% sai por apenas R${:.2f}!'.format(preco,desconto))