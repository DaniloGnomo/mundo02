from datetime import date

ano_atual = date.today().year
ano_nasci = int(input('\33[1;35mInsira o ano de nascimento com 4 digitos: \33[m'))
idade = ano_atual-ano_nasci
if idade <= 9:
<<<<<<< HEAD
    print('\33[1;32mVocê tem {} anos e esta na categoria MIRIM!\33[m'.format(idade))
elif 9 < idade <= 14:
    print('\33[1;34mVocê tem {} anose e esta na categoria INFANTIL!\33[m'.format(idade))
elif 14 < idade <= 19:
    print('\33[1;33mVocê tem {} anos e esta na categoria JUNIOR\33[m'.format(idade))
elif 19 < idade <= 20:
    print('\33[1;32mVocê tem {} e esta na categoria SÊNIOR\33[m'.format(idade))
elif idade > 20:
    print('\33[1;37mVocê tem {} e esta na categoria MASTER\33[m'.format(idade))
=======
    print('\33[1;32mVocê esta na categoria MIRIM!')
elif 9 < idade <= 14:
    print('\33[1;34mVocê esta na categoria INFANTIL!\33[m')
elif 14 < idade <= 19:
    print('\33[1;33mVocê esta na categoria JUNIOR\33[m')
elif 19 < idade <= 20:
    print('\33[1;32mVocê esta na categoria SÊNIOR\33[m')
elif idade > 20:
    print('\33[1;37mVocê esta na categoria MASTER\33[m')
>>>>>>> 620c3b27416c76e4639a7ce9f37a64aff19ba596
