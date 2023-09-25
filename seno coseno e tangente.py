from math import sin, cos, tan, radians
an = float(input('digite um angulo: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('o angulo de {}\n tem o seno de {:.2f}\n tem o cosseno de {:.2f}\n tem a tangente de {:.2f}'.format(an, seno, cosseno, tangente))
