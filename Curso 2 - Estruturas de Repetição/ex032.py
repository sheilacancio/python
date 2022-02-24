print('Exercício 32')

#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

print('Maior e menor valor')
print()

v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
v3 = int(input('Digite o 3° valor: '))

menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3
print('O menor valor que você digitou foi {}'.format(menor))

print()
maior = v1
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3
print('O maior valor que você digitou foi {}'.format(maior))
