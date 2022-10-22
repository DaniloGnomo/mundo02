from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('\33[1;34mDigite o ano de seu nascimento com quatro digitos: \33[m'))
idade = ano_atual-ano_nascimento
if idade < 18:
    print('\33[1;33mVocê tem {} anos e não possui idade suficiente para se alistar, faltam {} anos para isso\33[m'.format(idade, 18-idade))
elif idade == 18:
    print('\33[1;32mVocê tem ou ira completar 18 anos em {} você ja pode se alistar!\33[1;34m'.format(ano_atual))
elif idade > 18:
    print('\33[1;35mVocê já possui {} anos e já passou {} anos do prazo de inscrição\33[m'.format(idade, idade-18))
