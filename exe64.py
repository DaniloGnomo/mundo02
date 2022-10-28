num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('DIGITE UM NUMERO, QUALQUER\nLEMBRANDO QUE O NUMERO 999 ENCERRA O PROGRAMA\nNUMERO =  '))
    if num == 999:
        print('Foram digitados {} NUMEROS e soma destes numeros foi: {}'.format(cont, soma))
    else:
        cont += 1
        soma += num
