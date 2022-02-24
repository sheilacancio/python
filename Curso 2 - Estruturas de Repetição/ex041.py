print('Exercício 41')

#Mostre a tabuada de um número que o usuário escolher, utilizando o laço de repetição FOR.

print('TABUADAS')

n = int(input('Digite um número para exibir a tabuada correspondente: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(n, c, n*c))

