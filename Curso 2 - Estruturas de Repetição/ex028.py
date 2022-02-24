import random

print('Exercício 28')

#Escreva um programa que leia a velocidade de um carro.
    #Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    #A multa vai custar R$7,00 por cada Km acima do limite.

print('Radar Eletrônico')

veloc = random.uniform(70, 100)
print('Sua velocidade atual é {:.1f}Km/h'.format(veloc))
print()

if veloc > 80.0:
    print('Você excedeu o limite de velocidade de 80Km/h!')
    limite = (veloc - 80)
    multa = limite * 7
    print('Você ultrapassou {:.1f}Km e receberá uma multa no valor de R${:.2f}'.format(limite, multa))
else:
    print('Velocidade permitida!')

