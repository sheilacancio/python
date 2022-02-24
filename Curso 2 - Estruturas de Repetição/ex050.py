print('Exercício 50')
print('| TABUADA v3.0')

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Escolha um número para exibir a tabuada: '))
    if num < 0:
        break
    print('=' * 43)
    for cont in range(0, 11):
        print('{} x {} = {}'.format(num, cont, num*cont))
    print('=' * 43)
print('EXIBIÇÃO DE TABUADAS ENCERRADA!')

