#Exercício 53

#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    #Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.

print('| NÚMERO POR EXTENSO | ')
print()

numerais = ('zero','um','dois','três','quatro','cinco,','seis','sete','oito','nove','dez',
            'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:  # while faz a validação do número digitado
    n = int(input('Digite um número de 0 a 20: '))
    if 0 <= n <= 20:
        break
    print('Número inválido, tente novamente. ', end='')




