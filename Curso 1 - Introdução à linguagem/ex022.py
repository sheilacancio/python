print('Exercício 22')

#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
    #EX: Digite um número: 1834

    # unidade: 4
    # dezena: 3
    # centena: 8
    # milhar: 1

num = int(input('Digite um número de 0 a 9999: '))

uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))