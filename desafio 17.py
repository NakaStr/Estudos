import math
ang = int(input('Digite o Angulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cosseno = math.cos(rad)
tange = math.tan(rad)
print('O seno é: {} \nO cosseno é: {} \nA tangente é: {}'.format(seno, cosseno, tange))
