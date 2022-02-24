import random
print('Exercício 51')
print()

#Faça um programa que jogue par ou ímpar com o computador.
#o jogo será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print('| JOGO DO PAR OU ÍMPAR |')

vitória = 0

while True:
    print('=' * 25)
    jogador = int(input('Escolha um número: '))
    computador = random.randint(0, 10)
    soma = jogador + computador
    palpite = ' '
    while palpite not in 'PpIi':
        palpite = str(input('PAR ou ÍMPAR? [P / I] ')).strip().upper()
    print('Você jogou {} e o computador jogou o número {}. O total foi {}!'.format(jogador, computador, soma))

    if palpite == 'P':
        if soma % 2 == 0:
            print('Deu par, você GANHOU!')
            vitória = vitória + 1
        else:
            print('Você PERDEU!')
            break
    elif palpite == 'I':
        if soma % 2 == 1:
            print('Deu ímpar, você GANHOU!')
            vitória = vitória + 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente?...')
print('GAME OVER! VOCÊ VENCEU {} VEZES.'.format(vitória))











