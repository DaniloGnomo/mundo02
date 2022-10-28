count = 0
fim = 1
continua = 1
reslt = 0
while fim != 0:
    prtm = int(input('Digite o primeiro termo: '))
    raz = int(input('Digite a razão: '))
    while count != 10:
        count += 1
        prtm += raz
        print(prtm, end=' / ')
    while continua != 0:
        continua = int(input('\nVocê deseja ver mais quantos termos\nDigite 0 (zero) para encerrar: '))
        if continua >= 1:
            count2 = 0
            while count2 != continua:
                count2 += 1
                prtm += raz
                print(prtm, end=' / ')

    else:
        fim = 0
        print('PROGRAMA ENCERRADO')
