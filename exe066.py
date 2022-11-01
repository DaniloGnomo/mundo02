cont = soma = 0
while cont != 999:
    num = int(input('\33[1;34mDigite um valor (999 para parar): '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'A soma dos {cont} valores foi {soma}!')
