import datetime
print('Exercício 35')

#Faça um programa que leia o ano de nascimento de um jovem do sexo masculino e informe, de acordo com sua idade:
    #Se ele ainda vai se alistar ao serviço militar.
    #Se é a hora de se alistar.
    #Se já passou do tempo de alistamento.
#Seu programa também deverá mostra o tempo que falta ou que passou do prazo.

print('| ALISTAMENTO MILITAR |')

nome = str(input('Digite seu nome completo: ')).strip()
print('Olá, Sr. {}!'.format(nome))

data_atual = datetime.date.today()
nascimento = int(input('Ano de nascimento: '))
data = data_atual.year
idade = data - nascimento

if idade < 18:
    print('Ao completar a maioridade, aliste-se ao serviço militar!')
elif idade == 18:
    print('Chegou a hora do seu alistamento militar!')
else:
    saldo = idade - 18
    print('Passou o tempo do seu alistamento no serviço militar!')
    print('Tempo excedido: {} anos.'.format(saldo))





