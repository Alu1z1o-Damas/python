larg = float(input('Largura da parade: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área e de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisara de {}l de tinta.'.format(tinta))