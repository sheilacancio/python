#Exercício 56

#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    # Quantas vezes apareceu o valor 9.
    # Em que posição for digitado o valor 3.
    # Quais foram os números pares.

par = 0

print('| ANÁLISE DE DADOS EM UM TUPLA |')
print()
valores = (int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')),
           int(input('Digite um valor: ')))
print()
print('Você digitou os seguintes valores: {}'.format(valores))
print('O número 9 apareceu {} vezes.'.format(valores.count(9)))
if 3 in valores:
    print('O número 3 apareceu na {}ª posição.'.format(valores.index(3)+1))
else:
    print('O valor 3 não foi atribuído a nenhuma posição.')
for n in valores:
    if n % 2 == 0:
        par = par + 1
print('Foram digitados {} números pares.'.format(par))