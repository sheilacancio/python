print('Exercício 7')

#Faça um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor.

n = int(input('Digite aqui o número desejado: '))

ant = n - 1
suc = n + 1

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}!'.format(n, ant, suc))

    #Segunda opção, somente com uma variável:

    #n = int(input('Digite aqui o número desejado: '))
    #print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}!'.format(n, (n-1), (n+1)))

    #Nesta opção, a vantagem é economizar memória do dispositivo por ter somente uma variável e
    #como o objetivo é apenas mostrar os valores, não há necessidade, a não ser que as outras variáveis sejam usadas
    #posteriormente.




