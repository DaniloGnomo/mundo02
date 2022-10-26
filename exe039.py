from datetime import date
<<<<<<< HEAD
ano_atual = date.today().year
print('\33[1;32mEscolha ( 1 ) para sexo Masculino\n'
      '        ( 2 ) para sexo Feminino:\33[m')
sexo = int(input('Qual a sua escolha: '))
if sexo == 1:
    ano_nascimento = int(input('\33[1;34mDigite o ano de seu nascimento com quatro digitos: \33[m'))
    idade = ano_atual - ano_nascimento

    if idade < 18:
        print('\33[1;33mVocê tem {} anos e não possui idade suficiente para se alistar,\n'
              'Faltam {} anos para isso e sera no ano de {}\33[m'.format(idade, 18-idade, ano_nascimento + 18))
    elif idade == 18:
        print('\33[1;32mVocê tem ou ira completar 18 anos em {} você ja pode se alistar!\33[1;34m'.format(ano_atual))
    elif idade > 18:
        print('\33[1;35mVocê já possui {} anos e já passou {} anos do prazo de inscrição\n'
              'O ano de seu alistamento foi em {}\33[m'.format(idade, idade-18, ano_nascimento + 18))
else:
    print('\33[1;31mPessoas do sexo Feminino não precisam fazer o alistamento!\33[m')
=======

ano_atual = date.today().year
ano_nascimento = int(input('\33[1;34mDigite o ano de seu nascimento com quatro digitos: \33[m'))
idade = ano_atual-ano_nascimento
if idade < 18:
    print('\33[1;33mVocê tem {} anos e não possui idade suficiente para se alistar, faltam {} anos para isso\33[m'.format(idade, 18-idade))
elif idade == 18:
    print('\33[1;32mVocê tem ou ira completar 18 anos em {} você ja pode se alistar!\33[1;34m'.format(ano_atual))
elif idade > 18:
    print('\33[1;35mVocê já possui {} anos e já passou {} anos do prazo de inscrição\33[m'.format(idade, idade-18))
>>>>>>> 620c3b27416c76e4639a7ce9f37a64aff19ba596
