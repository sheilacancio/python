import random

print('Exercício 20')

#O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
    #Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

print('| A P R E S E N T A Ç Õ E S |')

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

lista = [a1, a2, a3, a4]
random.shuffle(lista)  #shuffle embaralha a lista

print('A ordem sorteada é a seguinte:')
print(lista)