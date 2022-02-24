print('Exercício 29')

#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

print('Par ou Ímpar?')

num = int(input('Digite um número inteiro: '))
resto = num % 2

if resto == 0:
    print('O número escolhido é PAR!')
else:
    print('O número escolhido é ÍMPAR!')