n1 = 0
n2 = 0
opera = 0
maior = 0
esc = 0
while esc != 5 or esc == 4:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite um outro valor: '))
    esc = int(input('Escolha: \n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NUMEROS\n[5] SAIR\nSua escolha: '))
    if esc == 1:
        opera = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, opera))
    if esc == 2:
        opera = n1 * n2
        print('A multiplicação de {} por {} é = {}'.format(n1, n2, opera))
    if esc == 3:
        if n1 > maior:
            maior = n1
        if n2 > maior:
            maior = n2
        print('Entre {} e {} o maior numero é {}'.format(n1, n2, maior))
print('PROGRAMA  ENCERRADO')


