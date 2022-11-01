cont = ''
total = lista = 0

print('-'*25)
print('LOJA SUPER BARATÃO')
print('-'*25)
while cont != 'N':
    produto = input('Nome do Produto: ').upper()
    preco = float(input('Preço: R$ '))
    if lista == 0:
        lista += 1
        prodbar = preco
        nombar = produto
        prodmil = 0
    if prodbar > preco:
        prodbar = preco
        nombar = produto
    if preco > 1000:
        prodmil += 1
    total += preco
    cont = input('Quer Continuar? [S/N] ').upper()
    if cont in ('SN'):
        cont = cont
    else:
        cont = input('Quer Continuar? [S/N] ').upper()
    if cont == ('S'):
        cont = cont
    else:
        break
print(f'--------------FIM DO PROGRAMA-----------------\n'
      f'Total gasto: R$ {total}\n'
      f'{prodmil} Produtos custaram mais de R$ 1.000,00\n'
      f'O produto mais barato foi: {nombar}')
