print('Exercício 24')

#Crie um programa que leia o nome de uma pessoa e dise se ela tem "SILVA" no nome.

nome = str(input('Nome completo: ').strip())

print('Tem Silva no seu nome? {}'.format('SILVA' in nome.upper()))
