print('Exercício 10')

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# 1 US$ = R$ 5.43

real = float(input('Digite o valor em reais: R$ '))
dolar = float(input('Digite a cotação atual do dólar: US$ '))

conversao = real / dolar

print('O valor convertido em dólares é igual a: {:.2f}'.format(conversao))

