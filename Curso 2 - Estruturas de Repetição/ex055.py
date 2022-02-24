import random

#Exercício 55

#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
    # Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

print('| MAIOR E MENOR VALOR EM TUPLA |')
print()

valores = (random.randint(0, 50), random.randint(0, 50), random.randint(0, 50), random.randint(0, 50), random.randint(0, 50))
print('Os valores sorteados foram: {}'.format(valores), end='')
print('\nO MAIOR valor sorteado foi: {}'.format(max(valores)))
print('O MENOR valor sorteado foi: {}'.format(min(valores)))



