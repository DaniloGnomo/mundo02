num = 0
while num >= 0:
    num = int(input('\33[1;36mQuer ver a tabuada de qual valor? '))
    print('\33[1;32m-' * 35)
    cont = 0
    if num >= 0:
        while cont in range(0, 9):
            cont += 1
            print(f'\33[1;34m{num} X {cont} = {num * cont}')
    else:
        break
print('\33[1;35mPROGRAMA TABUADA ENCERRADO!\33[M')
