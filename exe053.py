frase = input('DIGITE UMA FRASE: ').upper()
txt = frase.replace(' ', '')
txt2 = txt[::-1]
print(txt, txt2)
if txt == txt2:
    print('A FRASE É UM PALINDROMO')
else:
    print('A FRASE NÃO É UM PALINDROMO')
