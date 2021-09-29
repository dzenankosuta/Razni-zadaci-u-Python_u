#Dobijanje Pravougaonika

a=int(input('Unesite prvu potencijalnu stranicu pravougaonika: '))
b=int(input('Unesite drugu potencijalnu stranicu pravougaonika: '))
c=int(input('Unesite trecu potencijalnu stranicu pravougaonika: '))
d=int(input('Unesite cetvrtu potencijalnu stranicu pravougaonika: '))

if a==b==c==d:
    print('Moze')
elif a==b and c==d:
    print('Moze')
elif a==c and b==d:
    print('Moze')
elif a==d and b==c:
    print('Moze')
else:
    print('Ne moze')

