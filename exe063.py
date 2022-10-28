print('\33[1;32m*** SEQUENCIA DE FIBONACCI ***\33[m')
num = int(input('\33[1;35mDIGITE O NUMERO DE TERMOS: \33[m'))
f1 = 0
f2 = 1
print(f1, '-', f2, end=' - ')
cont = 2
while cont < num:
    cont += 1
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f3, end=' - ')
print('Esses são os {} primeiros termos'.format(num))
