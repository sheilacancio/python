from math import trunc

print('Exercício 16')

#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
    #EX: Digite um número: 6.127
    #O número 6.127 tem a parte inteira 6.
    # trunc retorna a proção inteira de um número real

print('| A R R E D O N D A M E N T O |')
num = float(input('Digite um número real: '))
parte_inteira = trunc(num)
print('O número {} tem a parte inteira {}.'.format(num,parte_inteira))

