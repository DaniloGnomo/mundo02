from time import sleep
import random
jogador = 'TESOURA'
maquina = 'TESOURA'
esc_maquina = (random.randint(1, 3))
esc_jogador = int(input('\33[1;34mEscolha (1) para PEDRA\33[m\n'
                    '\33[1;36mEscolha (2) para PAPEL\33[m\n'
                    '\33[1;35mEscolha (3) para TESOURA\33[m\n'
                    '\33[1;32mQual a sua escolha: \33[m'))
print('\33[1;31mJO\33[m')
sleep(0.50)
print('\33[1;32mKEN\33[m')
sleep(0.40)
print('\33[1;33mPO\33[m')
sleep(0.30)
if esc_jogador == 1:
    jogador = 'PEDRA'
if esc_jogador == 2:
    jogador = 'PAPEL'
if esc_jogador == 3:
    jogador = 'TESOURA'
if esc_maquina == 1:
    maquina = 'PEDRA'
if esc_maquina == 2:
    maquina = 'PAPEL'
if esc_maquina == 3:
    maquina = 'TESOURA'
if esc_jogador == 1 and esc_maquina == 3 or esc_jogador == 2 and esc_maquina == 1 or esc_jogador == 3 and esc_maquina == 2:
    print('\33[1;32mJOGADOR\33[m {} X {} \33[1;34mCOMPUTADOR\33[m\n'
          'PARABENS VOCÊ VENCEU !'.format(jogador, maquina))
elif esc_maquina == 1 and esc_jogador == 3 or esc_maquina == 2 and esc_jogador == 1 or esc_maquina == 3 and esc_jogador == 2:
    print('\33[1;32mJOGADOR\33[m {} X {} \33[1;34mCOMPUTADOR\33[m\n'
          'TENTE NOVAMENTE O COMPUTADOR VENCEU!'.format(jogador, maquina))
elif esc_maquina == esc_jogador:
    print('\33[1;32mJOGADOR\33[m {} X {} \33[1;34mCOMPUTADOR\33[m\n'
          'EMPATE, NINGUEM VENCEU!'.format(jogador, maquina))
