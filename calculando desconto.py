preço = float(input('qual o preço do seu produto? R$'))
novo = preço - (preço * 13 / 100)
print('O produto custava {}R$ na promoção vai sair por {}R$'.format(preço, novo))