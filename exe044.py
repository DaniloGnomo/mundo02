preco_normal = float(input('\33[1;32mQual o valor do produto: R$ \33[m'))
forma_pagamento = int(input('\33[1;33mEscolha a forma de pagamento\n'
                        '(1) para pagamento a vista em dinheiro ou cheque\n'
                        '(2) para pagamento a vista com cartão\n'
                        '(3) para pagar em 2x no cartão de credito\n'
                        '(4) para pagar em 3x ou mais no cartão de credito \33[m'))
if forma_pagamento == 1:
    print('Para pagamento a vista você tem um desconto de 10%\n'
          'Você ira pagar R$ {:.2f}'.format(preco_normal-(preco_normal*10/100)))
elif forma_pagamento == 2:
    print('Para pagamento a vista no cartão você tem um desconto de 5%\n'
          'Você ira pagar R$ {:.2f}'.format(preco_normal-(preco_normal*5/100)))
elif forma_pagamento == 3:
    print('Pagando em 2x você não paga juros\n'
          'Você ira pagar 2 parcelas de R$ {:.2f}'.format(preco_normal/2))
elif forma_pagamento == 4:
    parc = int(input('\33[1;36mQual o numero de parcelas que vc deseja pagar:\33[m '))
    print('Para pagamentos superiores a 3x ha um acrecimo de 20%, pagando em {} vezes\n'
          'Você ira pagar {} parcelas de R$ {:.2f}'.format(parc, parc, ((preco_normal+preco_normal*20/100)/parc)))
else:
    print('Digite uma opção valída !')
