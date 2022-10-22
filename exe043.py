peso = float(input('\33[1;36mDigite o seu peso: \33[m'))
altura = float(input('\33[1;36mDigite a sua altura: \33[m'))
imc = peso / (altura * altura)
if imc <= 18.5:
    print('\33[0;32m Você esta a baixo do seu IMC ideal\n'
          'Seu peso ideal seria entre {:.2f} Kg e {:.2f} Kg\33[m'.format(18.5 * (altura ** 2), 25 * (altura ** 2)))
elif (imc > 18.5) and (imc <= 25):
    print('\33[0;33m Você esta com o seu IMC em {:.2f} que é o ideal\n'
          'Você esta entre 18.5 e 25 de IMC \33[m'.format(imc))
elif (imc > 25) and (imc <= 30):
    print('\33[0;34m Você esta com sobrepeso do seu IMC ideal\n'
          'Seu peso ideal seria entre {:.2f} Kg e {:.2f} Kg\33[m'.format(18.5 * (altura ** 2), 25 * (altura ** 2)))
elif (imc > 30) and (imc <= 40):
    print('\33[0;36m Você esta com Obesidade referente ao seu IMC ideal\n'
          'Seu peso ideal seria entre {:.2f} Kg e {:.2f} Kg\33[m'.format(18.5 * (altura ** 2), 25 * (altura ** 2)))
elif imc > 40:
    print('\33[0;37m Você esta com Obesidade Mórbida em relação ao seu IMC ideal\n'
          'Seu peso ideal seria entre {:.2f} Kg e {:.2f} Kg\33[m'.format(18.5 * (altura ** 2), 25 * (altura ** 2)))
