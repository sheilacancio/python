print('Exercício 33')

#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.
    #O programa vai perguntar o VALOR da casa, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.
    #Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1;97;44m| BANCO SCS |\033[m')
print()

nome = str(input('Nome completo: ')).strip()
print('Olá, Sr(a) {}!'.format(nome))
print()

print('Antes de avaliarmos o seu empréstimo bancário, precisamos das seguintes informações:')
imovel = float(input('Qual o valor do imóvel desejado? R$ '))
salario = float(input('Qual sua renda mensal? R$ '))
anos = int(input('Quantos anos de financiamento: '))
parcela = imovel / (anos * 12)
print()

print('Para financiar um imóvel no valor de R${:.2f} em {} anos, serão feitas parcelas no valor de R${:.2f}.'.format(imovel, anos, parcela))

percentual = salario * 30 / 100

if parcela <= percentual:
    print('\033[1;30;42mPARABÉNS! Seu empréstimo foi aprovado!\033[m')
else:
    print('\033[1;30;41mDesculpe, mas o valor do parcelamento excedeu 30% da sua renda mensal, por isso seu empréstimo foi negado!\033[m')












