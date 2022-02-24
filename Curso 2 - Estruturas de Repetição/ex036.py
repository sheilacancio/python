print('Exercício 36')

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida:

print('MÉDIA DAS NOTAS')

m1 = float(input('Primeira nota: '))
m2 = float(input('Segunda nota: '))
media = (m1 + m2) / 2
print()

if media >= 7.0:
    print('\033[1;30;42mPARABÉNS! Sua média foi {:.1f}, você foi APROVADO(A)!\033[m'.format(media))
elif media < 5.0:
    print('\033[1;30;41mSua média foi {}, portanto você foi reprovado(a)!\033[m'.format(media))
elif media >= 5.0 or media <= 6.9:
    print('\033[1;30;43mSua média foi {:.1f}, portanto você esta de recuperação!\033[m'.format(media))



