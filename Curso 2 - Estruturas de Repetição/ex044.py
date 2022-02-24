print('Exercício 44')

#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('| NÚMEROS PRIMOS |')
print()

num = int(input('Digite um número inteiro: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print()
print('\n\033[mO número {} pode ser dividido {} números.'.format(num, total))

if total == 2:
    print('O valor digitado é \033[32mPRIMO!\033[m')
else:
    print('O valor digitado \033[31mNÃO É PRIMO\033[m, pois é divisível por mais de 2 números!')