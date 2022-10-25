numero = int(input('\33[1;38mDIGITE UM NUMERO INTEIRO: \33[m'))
print('\33[1;36mESCOLHA UMA DAS OPÇÕES ABAIXO\33[m\n'
      '\33[0;32m( 1 ) Converter para BINÁRIO \33[m\n'
      '\33[0;35m( 2 ) Converter para OCTAL \33[m\n'
      '\33[0;33m( 3 ) Converter para HEXADECIMAL \33[m')
conv = int(input('\33[1;31mQUAL OPÇÃO VOCÊ DESEJA ESCOLHER: \33[m'))
if conv == 1:
    print('O número {} em Binário é: {}'.format(numero, bin(numero)[2:]))
elif conv == 2:
    print('O número {} em Octal é: {}'.format(numero, oct(numero)[2:]))
elif conv == 3:
    print('O número {} em hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('\33[1;38mVOCÊ ESCOLHEU UMA OPÇÃO INCORRETA\33[m')
