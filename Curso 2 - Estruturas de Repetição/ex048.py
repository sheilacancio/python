print('Exercício 48')

print('| PROGRESSÃO ARITMÉTICA v2.0 |')
'''print()

primeiro = int(input('1º termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('FIM')'''

primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão

termo = primeiro
contador = 1

while contador <= 10:
    print('{} | '.format(termo), end='')
    termo = termo + razão
    contador = contador + 1
