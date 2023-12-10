distancia = float(input('Qual é a distancia da sua viage? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('É o proço da sua passagem será de R${:.2f}'.format(preço))     