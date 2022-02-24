import random

print('Exercicio 19')

#Um professor quer sortear um de seus alunos para apagar o quadro.
    #faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido(a).

print('Sorteio')

a1 = input('Nome do 1º aluno(a): ')
a2 = input('Nome do 2º aluno(a): ')
a3 = input('Nome do 3º aluno(a): ')
a4 = input('Nome do 4º aluno(a): ')

lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)

print('O aluno(a) sorteado foi: {}'.format(sorteio))