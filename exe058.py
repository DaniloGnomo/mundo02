import random
palp = 0
papc = random.randint(0, 10)
tent = 0
cont = 'S'
while palp != papc:
    palp = int(input('Tente adivinhar o numero do computador\n Sua escolha: '))
    tent += 1
    if palp == papc:
        print('Você acertou o numero era {} você usou {} tentativas'.format(papc, tent))
