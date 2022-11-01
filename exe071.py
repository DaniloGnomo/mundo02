print('='*25)
print('BANCO ONLY MONEY')
print('='*25)
valor = int(input('Que valor você que sacar?\n\33[1:33mLIMITE DE R$ 9.999,00\33[m R$ '))
total = valor
notas = 50
totalnotas = 0
while True:
    if total >= notas:
        total -= notas
        totalnotas += 1
    else:
        if totalnotas > 0:
            print(f'Total de {totalnotas} de R$ {notas:.2f}')
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totalnotas = 0
        if total == 0:
            break
