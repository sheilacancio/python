print('Exercício 14')

#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para Fahrenheit.
# F = C x 1,8 + 32

print('CONVERSOR DE TEMPERATURAS')
celsius = float(input('Temperatura em ºC: '))
fahrenheit = celsius * 1.8 + 32

print('A temperatura de {}ºC corresponde a {}ºF'.format(celsius,fahrenheit))