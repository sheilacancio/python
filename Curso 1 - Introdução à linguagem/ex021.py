print('Exercício 21')

#Crie um programa que leia o nome completo de uma pessoa e mostre:
    # O nome com todas as letras maiúsculas
    # O nome com todas as letras minúsculas.
    #Quantas letras tem (sem adicionar espaços)
    #Quantas letras tem o primeiro nome.

print('CARACTERÍSTICAS DO SEU NOME')
nome = input('Digite seu nome completo: ')

print("Seu nome em letras maiúsculas é: {}".format(nome.upper()))

print("Seu nome em letras minúsculas é: {}".format(nome.lower()))

print("Ao todo, seu nome tem {} letras".format(len(nome.replace(' ',''))))

primeira_palavra = nome.split()
print("Seu primeiro nome tem {} letras".format(len(primeira_palavra[0])))