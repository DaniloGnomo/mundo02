media = 0
cont = ''
count = 0
soma = 0
while cont != 'N':
    num = int(input('DIGITE UM NUMERO: '))
    count += 1
    soma += num
    if count == 1:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    media = soma / count
    print('DESEJA CONTINUAR ?')
    cont = input('(S) ou (N) ').upper()
    if cont == 'S':
        cont = 'S'
else:
    print('A MEDIA de todos os {} valores\nFoi {} / {} = {}\nO maior valor foi {}\n'
          'O menor valor foi {}'.format(count, soma, count, media, maior, menor))


