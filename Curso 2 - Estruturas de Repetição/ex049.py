print('Exercício 49')

#Crie um programa que leia VÁRIOS NÚMEROS inteiros pela teclado.
#O programa só vai para quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA.
#No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderando o flag)

print('| VÁRIOS NÚMEROS COM FLAG |')
soma = 0
contador = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    soma = soma + n
    contador = contador + 1
print('A soma dos {} valores foi igual a {}'.format(contador,soma))

