sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('\33[1;33mEscolha [M] Masculino ou [F] Feminino: \33[m').strip().upper()[0]
    print('\33[1;31mFaça uma escolha correta\33[m')
else:
    print('\33[1;35m{} é uma escolha valida\33[m'.format(sexo))
