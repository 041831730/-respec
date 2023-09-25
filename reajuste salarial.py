nome = input('qual seu produto? ')
prod = float(input('qual o valor do produto? R$'))
ifood = prod + (prod * 20 / 100)
print(' o  {} que custava {:.2f}R$\n vai custar no ifood  {:.2f}R$'.format(nome, prod, ifood))