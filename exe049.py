tab = int(input('Digite a tabuada desejada: '))
print('#'*15)
for c in range(1, 11):
    tabr = tab * c
    print('# {} X {:2} = {:2} #'.format(tab, c, tabr))
print('#'*15)
