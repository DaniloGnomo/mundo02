nota_1 = float(input('\33[1;32mInsira sua primeira nota: \33[m'))
nota_2 = float(input('\33[1;33mInsira sua segunda nota: \33[m'))
media = (nota_1+nota_2)/2
if media < 5.0:
    print('\33[1;31mMedia {} REPROVADO!\33[m'.format(media))
elif media == 5.0 or media <= 6.9:
    print('\33[1;33mMedia {} RECUPEÇÃO estude mais!'.format(media))
elif media >= 7.0:
    print('\33[1;32mMedia {} APROVADO\33[m'.format(media))
