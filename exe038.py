n1 = int(input('\33[1;34mDigite um numero inteiro qualquer: \33[m'))
n2 = int(input('\33[1;35mDigite outro numero inteiro qualquer: \33[m'))

if n1 == n2:
    print('\33[0;34mNão existe valor maior os numeros são iguais!\33[m')
elif n1 > n2:
    print('\33[0;37mO primeiro valor é maior\33[m')
else:
    print('\33[0;36mO segundo valor é maior\33[m')
