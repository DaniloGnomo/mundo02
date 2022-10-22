lado_a = float(input('\33[1;32mDigite o valor do primeiro lado: \33[m'))
lado_b = float(input('\33[1;33mDigite o valor do segundo lado: \33[m'))
lado_c = float(input('\33[1;34mDigite o valor do terceiro lado: \33[m'))
triangulo = lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b
if triangulo:
    if lado_a == lado_c and lado_a == lado_b and lado_c == lado_b:
        print('As medidas formam um triangulo Equilátero, \n'
              ' todos os lados são iguais A {} B {} C{}'.format(lado_a, lado_b, lado_c))

    if lado_a == lado_b != lado_c or lado_b == lado_c != lado_a or lado_a == lado_c != lado_c:
        print('A medidas formam um triangulo Isóceles\n'
              'Dois lados são iguais é um diferente A {} B {} C {}'.format(lado_a, lado_b, lado_c))
    if lado_a != lado_b and lado_a != lado_c and lado_c != lado_b:
        print('As medidas formam um triangulo escaleno\n'
              'Todos os lados são diferentes A {} B {} C {}c'.format(lado_a, lado_b, lado_c))
else:
    print('\33[1;35mAs medidas A {} B {} C {} não formam um triangulo\33[m'.format(lado_a, lado_b, lado_c))
