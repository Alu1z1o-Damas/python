<<<<<<< HEAD
frase = str(input('Digite uma frase: ')).upper()
=======
frase = str(input('Digite uma frase: ')).upper().strip()
>>>>>>> 02d210046d0a919253557c01025ed9fbeb70ac10
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))