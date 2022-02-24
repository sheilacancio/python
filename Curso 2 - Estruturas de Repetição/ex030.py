print('Exercício 30')

#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
    #R$0,50 por Km para viagens de até 200Km  e R$0,45 para viagens mais longas.

print('Custo da Viagem')

distancia = int(input('Qual a distância da sua viagem em Km? '))
print()

print('Valor da passagem:')
if distancia <= 200:
    valor1 = distancia * 0.50
    print('O valor total da passagem é de R${:.2f}'.format(valor1))
else:
    valor2 = distancia * 0.45
    print('O valor total da passagem é de R${:.2f}'.format(valor2))