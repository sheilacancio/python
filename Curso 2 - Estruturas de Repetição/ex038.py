import time
from time import sleep

print('Exercício 38')

#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0.
#com uma pausa de 1 segundo entre eles.

print('* CONTAGEM REGRESSIVA DOS FOGOS *')

for contagem in range(10, -1, -1):
    time.sleep(1)
    print(contagem)
print('FIIIM')