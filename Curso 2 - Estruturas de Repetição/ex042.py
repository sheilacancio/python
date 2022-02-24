print('Exercício 42')

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar, desconsidere-o.

print(' | SOMA DOS PARES')

soma = 0
for contagem in range(1, 7):
    n = int(input('Digite o {} valor: '.format(contagem)))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos números digitados que são pares é igual a: {}'.format(soma))
