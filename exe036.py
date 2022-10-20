vlcasa = float(input('\33[0;34mDigite o Valor da casa que você deseja adquirir: R$ \33[m'))
sal = float(input('\33[0;33mQual o valor do seu salário: R$ \33[m'))
anos = int(input('\33[0;35mEm quantos anos você deseja pagar a casa: \33[m'))
vlprest = vlcasa/(anos*12)
psal = 30/100*sal
if vlprest <= psal:
    print('\33[0;34mParabens seu financiamento esta aprovado!\33[m\n'
          'Sua forma de pagamento será: {} prestações de R$ {:.2f}'.format(anos*12, vlprest))
else:
    print('\33[0;31mQue pena seu financiamento não pode ser aprovado\n'
          'O valor da prestação de R$ {:.2f} escede o valor limite de R$ {:.2f}\33[m'.format(vlprest, psal))
