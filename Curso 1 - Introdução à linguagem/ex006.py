print('Exercício 6 - Dissecando uma variável')

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

aleatorio = input('Digite algo: ')

print('É possível imprimir na tela? ', aleatorio.isprintable())

print('É alfanumérico? ', aleatorio.isalnum())
print('É alfa, contido no alfabeto? ', aleatorio.isalpha())

print('Contem somente letras minúsculas? ', aleatorio.islower())
print('Contem somente letras maiúsculas? ', aleatorio.isupper())

print('É um número? ', aleatorio.isnumeric())
print('É um número decimal? ', aleatorio.isdecimal())

print('É possível imprimir na tela? ', aleatorio.isprintable())



