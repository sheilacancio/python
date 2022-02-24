import random
print('Exercício 46')

#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print('JOGO DA ADIVINHAÇÃO v2.0')
print()
print('Seja bem-vindo(a) ao nosso jogo de adivinhação volume 2!!')
print('Agora, eu que sou o seu computador irei pensar em um número entre 0 e 10.')
print('Consegue adivinhar qual número pensei?')
print()

n = random.randint(0, 10)
print(n)
acertou = False
tentativas = 0
while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    tentativas = tentativas + 1
    if palpite == n:
        acertou = True
    else:
        if palpite < n:
            print('Dê um chute mais alto...está próximo!')
        else:
            print('Tente um número menor...')
print('Após {} tentativas, você acertou!'.format(tentativas))



