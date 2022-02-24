print('Exercício 13')

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo slário, com 15% de aumento.

print('REAJUSTE SALARIAL 2021')

salario = float(input('Salário atual: R$ '))
aumentar = salario * 15 / 100
aumento = salario + aumentar

print('Com o reajuste salarial de 15%, o seu salário que antes era R${:.2f}, aumentou para R${:.2f}'.format(salario, aumento))