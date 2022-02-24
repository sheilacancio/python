print('Exercício 11')

#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a qtd de tinta para pintá-la.
#OBS: Sabendo que cada litro de tinta consegue cobrir uma área de 2 metros quadrados.

print('Dimensões da parede:')

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
print('A dimensão da sua parede é de {}x{} e a sua área total é de {}m².'.format(largura, altura, area))

tinta = area / 2
print('Para pintar essa parede, você vai precisar de {}L de tinta'.format(tinta))