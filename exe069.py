print('-'*25)
print('CADASTRE UMA PESSOA')
print('-'*25)
cont = ''
cad = 0
while cont != 'N':
    cad += 1
    if cad == 1:
        cadh = cadm = qpes = 0
    idade = int(input('Idade: '))
    if idade in range(1, 120):
        idade = idade
    else:
        idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper()
    if sexo in ('MF'):
        sexo = sexo
    else:
        sexo = input('Sexo: [M/F] ')
    if idade > 18:
        qpes += 1
    if sexo == 'M':
        cadh += 1
    if sexo == 'F' and idade < 20:
        cadm += 1
    cont = input('Quer Continuar? [S/N]' ).upper()
    if cont in ('SN'):
        cont = cont
    else:
        cont = input('Quer Continuar? [S/N] ')
print(f'======FIM DO PROGRAMA======\n'
      f'Total de pessoas com mais de 18 anos: {qpes}\n'
      f'Ao todo temos {cadh} Homens cadastrados\n'
      f'E temos {cadm} Mulheres com menos de 20 anos.')

