from random import randint
from time import sleep
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