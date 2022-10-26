from datetime import date
maior = 0
menor = 0
anoat = date.today().year
for c in range(1, 8):
    ano = int(input('DIGITE O {}º ANO DE NASCIMENTO: '.format(c)))
    if (anoat - ano) >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('{} Pessoas não tem 18 anos'.format(menor))
print('{} Pessoas ja tem mais de 18 anos'.format(maior))
