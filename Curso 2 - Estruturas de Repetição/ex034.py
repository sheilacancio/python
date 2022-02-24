print('Exercício 34')

#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma das seguintes mensagens:
    # O primeiro valor é maior
    # O segundo valor é maior
    # Não existe valor maior, os dois são iguais

print('\033[1;40mComparando Números\033[m')
print()

v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))

if v1 > v2:
    print('\033[1;30;42mO primeiro valor é o maior, sendo ele {}.\033[m'.format(v1))
elif v1 == v2:
    print('\033[1;30;43mNão existe valor maior, os dois são iguais!\033[m')
else:
    print('\033[1;30;42mO segundo valor é o maior, sendo ele {}.\033[m'.format(v2))


