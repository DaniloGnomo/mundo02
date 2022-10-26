maior = 0
media = 0
idfemi = 0
mvelho = ''
for c in range(1, 5):
    print('DIGITE OS DADOS DA {}ª PESSOA'.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = int(input('Escolha ( 1 ) Masculino e ( 2 ) Feminino: '.format(c)))
    if c == 1:
        media = idade
    if sexo == 1 or sexo == 2:
        media = media + idade
    if c == 1 and sexo == 1:
        maior = idade
        mvelho = nome
    if sexo == 1 and idade > maior:
        mvelho = nome
        maior = idade
    if sexo == 2 and idade > 20:
        idfemi = idfemi +1
print('A media de idade do grupo é: {} anos.\n'
      'O homem mais velho tem {} anos e se chama {}.\n'
      'O grupo possui {} mulheres com mais de 20 anos'.format(media/5, maior, mvelho.upper(), idfemi))
