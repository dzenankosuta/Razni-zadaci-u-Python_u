#Nalazenje obima kruga preko povrsine

import math

P=float(input('Unesite povrsinu kruga:'))

r=math.sqrt(P/math.pi)

O=2*r*math.pi

print('Potreban obim iznosi:' ,format(O, '.2f'))
