print('Exercício 25')

#Faça um programa que leia uma frase pelo teclado e mostre:
    # Quantas vezes aparece a letra "A"
    # Em que posição ela aparece a primeira vez
    # Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()

print('A letra A aparece {} vezes.'.format(frase.count('A')))
print('A primeira ocorrência da letra A é na posição {}'.format(frase.find('A')))
print('A última vez que a letra A apareceu foi na posição {}'.format(frase.rfind('A')))