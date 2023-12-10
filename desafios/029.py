v = float(input('Qual é a velocidade atual do carro?')) 
if v > 80:
    print('MULTADO! Você exedeo o limite de velocidade permitido de 80Km\h!')
    multa = (v-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha un bom dia! Dirija com segurança!') 



