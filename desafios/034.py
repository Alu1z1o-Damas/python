salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 18 / 100)  
print('Quem ganhava R${:.2f} passa a quanhar R${:.2f} ')    
