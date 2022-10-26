p = 0
num = int(input('Digite um numero inteiro: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[1;33m', end=' ')
        p += 1
    else:
        print('\33[1;35m', end='.')
    print('{}'.format(c), end='')
print('\n\033[1;34mO numero \33[1;32m{}\33[1;34m foi divisivel \33[1;35m{}\33[1;34m vezes\33[m'.format(num, p))
if p == 2:
    print('\33[1;32mO numero \33[1;31m{}\33[1;32m é primo\33[m'.format(num))
else:
    print('\33[1;36mO numero \33[1;32m{}\33[1;34m não é primo\33[m'.format(num))
