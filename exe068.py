
from random import randint
print('\33[1;34m=-='*17)
print('\33[1;33mVAMOS JOGAR PAR OU ÍMPAR')
print('\33[1;34m=-='*17)
vit = jog = comp = cont = 0
derr = 1
escol = ''
while derr == 1:
    jog = int(input('\33[1;36mDigite um numero: '))
    escol = input('\33[1;35mPar ou Ímpar? [P / I]').upper()
    comp = randint(0, jog)
    if escol == 'P':
        if (jog + comp) % 2 == 0:
            vit += 1
            print(f'\33[1;33mVocê jogou {jog}\nO Computador jogou {comp}.\nTotal = {jog + comp}\33[1;32m DEU PAR')
            print('\33[1;36mVocê Venceu!')
        else:
            print(f'\33[1;34mVocê jogou {jog}\nO Computador jogou {comp}.\nTotal = {jog + comp}\33[1;35m DEU ÍMPAR')
            break
    else:
        if (jog + comp) % 2 != 0:
            vit += 1
            print(f'\33[1;33mVocê jogou {jog}\nO computador jogou {comp}.\nTotal = {jog + comp}\33[1;32m DEU ÍMPAR')
            print('\33[1;36mVocê Venceu!')
        else:
            print(f'\33[1;34mVocê jogou {jog}\nO computador jogou {comp}.\nTotal = {jog + comp}\33[1;35m DEU PAR')
            break
print('\33[1;36m=-='*17)
print(f'\33[1;32mGAME OVER!\nVocê Venceu {vit} vezes.')


