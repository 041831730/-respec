larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
area = larg * alt
print('sua area tem a dimensao de {}x{} e sua area e de {}m2 .'.format(larg, alt, area))
tinta = area / 2
print('para pintar sua parede voce vai precisar de {}l de tinta'.format(tinta))