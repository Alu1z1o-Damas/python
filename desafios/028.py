from random import randint
from time import sleep
<<<<<<< HEAD
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?'))
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÊNS! Você conseguiu me vencer!')
else:
    print('ERROU! Eu pensei no número {} e não no {}!'.format(computador, jogador))
        
=======
pc = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
game = int(input('Em que número eu panei?'))
print('PROCESSANDO...')
sleep(3)
if game == pc:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GAANHEI! Eu pensei no número {} e não no {}!'.format(pc, game))    
>>>>>>> 02d210046d0a919253557c01025ed9fbeb70ac10
