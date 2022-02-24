import datetime
print('Exercício 37')
print()

#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria de acordo com a sua idade.
    # Até 9 anos: mirim
    # Até 14 anos: infantil
    # Até 19 anos: junior
    # Até 20 anos: sênior
    # Acima de 20: master

print('\033[1;30;44m| CONFEDERAÇÃO NACIONAL DE NATAÇÃO |\033[m')
print()

print('Classificação dos atletas:')
ano_atual = datetime.date.today().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nascimento

if idade > 25:
    print('Idade: {} anos.'.format(idade))
    print('Classificação: MASTER')
elif idade <= 9:
    print('Idade: {} anos.'.format(idade))
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Idade: {} anos.'.format(idade))
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Idade: {} anos.'.format(idade))
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Idade: {} anos.'.format(idade))
    print('Classificação: SÊNIOR')