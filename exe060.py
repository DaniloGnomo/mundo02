fat = 1
res = 1
num = int(input('digite um numero: '))
while fat <= num:
    res *= fat
    fat += 1
    print(fat,  end=' ')
print('\nFatorial de {} é = {}'.format(num, res))
