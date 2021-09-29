#Ograda oko fudbalskog terena

d=int(input('Unesite duzinu terena: '))
s=int(input('Unesite sirinu terena: '))
r=int(input('Unesite rastojanje izmedju terena i ograde: '))

#Obim ograde racunamo tako sto na svaku duzinu(sirinu) dodamo jos rastojanje * 2

OO=2*d + 2*s + 8*r

print(OO)
