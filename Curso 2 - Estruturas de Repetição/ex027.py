import random
from random import randint

print('Exercício 27')

#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual
#foi o número escolhido pelo computador.
    #O computador deverá escrever na tela se o usuário venceu ou perdeu.

print('JOGO DA ADIVINHAÇÃO v1.0')

num = random.randint(0, 5)
print('Pense em um número inteiro entre 0 e 5')
escolhido = int(input('Digite o número pensado: '))
if num == escolhido:
    print('Você venceu! PARABÉNS!')
else:
    print('Você perdeu, na verdade o número sorteado foi {}! Não foi dessa vez :('.format(num))

