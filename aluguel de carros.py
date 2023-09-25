dias = int(input('quantos dias alugados? '))
km = float(input('quantos Km rodadados: '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é {:.2f}R$'.format(pago))