print('Exercício 40')

#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se estão no intervalo de 1 a 500.

print(' | SOMA DE ÍMPARES MÚLTIPLOS DE TRÊS |')

s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
print('A soma dos números ímpares é igual a {}'.format(s))
