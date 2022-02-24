print('Exercício 47')

#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

print('Criando um menu de opções')
print()

v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
print()
opção = 0
while opção != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MOSTRAR O MAIOR NÚMERO
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Escola uma opção: '))
    if opção == 1:
        soma = v1 + v2
        print('A soma entre os valores digitados é igual a: {}'.format(soma))
    elif opção == 2:
        mult = v1 * v2
        print('O resultado da multiplicação entre esses valor é igual a: {}'.format(mult))
    elif opção == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior valor é {}'.format(maior))
    elif opção == 4:
        print('Informe novos valores: ')
        v1 = float(input('Digite o primeiro valor: '))
        v2 = float(input('Digite o segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Digite novamente!')
print('Fim do programa!')