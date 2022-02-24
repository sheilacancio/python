# Exercício 58

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    #No final, mostre qual foi o maior e o menor valor valor digitado e suas respectivas posições na lista.

print('| MAIOR E MENOR VALOR EM UMA LISTA |')
print()
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor na posição {}: '.format(cont))))
print('=' * 32)
print('Valores listados: {}'.format(valores))
print('O maior valor digitado foi o {} na posição {}'.format(max(valores),valores.index(max(valores))))
print('O menor valor digitado foi o {} na posição {}'.format(min(valores),valores.index(min(valores))))
