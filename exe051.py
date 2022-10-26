print('\33[1;34mMOSTRANDO OS 10 PRIMEIROS TERMOS DE UMA PA\33[m')
pri_ter = int(input('Digite o primeiro termo da PA: '))
ra = int(input('Digite a progressão desejada: '))
for c in range(pri_ter, pri_ter+10*ra, ra):
    print(c, end=' / ')
