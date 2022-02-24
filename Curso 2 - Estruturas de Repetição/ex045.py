print('Exercício 45')

#Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F".
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

print('Validação de Dados')
print()

print('| CADASTRO DE GÊNERO | ')
sexo = str(input('Informe seu gênero [M/F]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Não foi possível computar a sua resposta, digite novamente!. Informe seu sexo: ')).strip().upper()
    if sexo == 'M' or 'F':
        print('Próxima etapa...')
print('Cadastro finalizado!')