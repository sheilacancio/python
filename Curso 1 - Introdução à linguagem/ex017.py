print('Exercício 15')

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a qtd de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('ALUGUEL DE CARROS')
dias = int(input('Quantos dias este carro foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
aluguel = (dias * 60) + (km * 0.15)

print('O valor do aluguel é de R${:.2f}'.format(aluguel))

