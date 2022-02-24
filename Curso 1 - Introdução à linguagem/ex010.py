print('Exercício 10')

#Escreva um programa que leia um valor em metros e exiba convertido em cm e mm.
    # km hm dam m dm cm mm

medida = float(input('Digite o valor em metros: '))

cm = medida * 100
mm = medida * 1000

print('A medida de {}m equivale a {:.0f}cm e {:.0f}mm.'.format(medida,cm, mm))


