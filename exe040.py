nota_1 = float(input('\33[1;32mInsira sua primeira nota: \33[m'))
nota_2 = float(input('\33[1;33mInsira sua segunda nota: \33[m'))
media = (nota_1+nota_2)/2
<<<<<<< HEAD
=======
#if 10 >= nota_1 >= 0 and 10 >= nota_2 >= 0:
>>>>>>> 620c3b27416c76e4639a7ce9f37a64aff19ba596
if media < 5.0:
    print('\33[1;31mMedia {} REPROVADO!\33[m'.format(media))
elif media == 5.0 or media <= 6.9:
    print('\33[1;33mMedia {} RECUPEÇÃO estude mais!'.format(media))
elif media >= 7.0:
    print('\33[1;32mMedia {} APROVADO\33[m'.format(media))
