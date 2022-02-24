print('Exercício 52')
print()
#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
    # quantas pessoas tem mais de 18 anos.
    # quantos homens foram cadastrados.
    # quantas mulheres tem menos de 20 anos.

pessoa = 0
maior18 = 0
mulher20 = 0
homem = 0
print('| ANÁLISE DE DADOS DO GRUPO |')

while True:
    nome = str(input('Seu primeiro nome: ')).strip()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Sexo [F / M]: ')).strip().upper()
    if idade >= 18:
        maior18 = maior18 + 1
    if sexo == 'M':
        homem = homem + 1
    if sexo == 'F' and idade < 20:
        mulher20 = mulher20 + 1
    escolha = str(input('Deseja continuar cadastrado pessoas? [S / N]: ')).strip().upper()
    if escolha == 'N':
        break
print('Cadastros encerrados!')
print()
print('ESTATÍSTICAS:')
print('Total de pessoas maiores de 18 anos: {} pessoas.'.format(maior18))
print('No total, foram cadastrados {} homens.'.format(homem))
print('O total de mulheres cadastradas com menos de 20 anos é igual a {}.'.format(mulher20))

