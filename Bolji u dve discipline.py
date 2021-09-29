#Bolji u dve discipline

a=int(input('Broj osvojenih poena prvog takmicara iz matematike: '))
b=int(input('Broj osvojenih poena prvog takmicara iz programiranja: '))
c=int(input('Broj osvojenih poena drugog takmicara iz matematike: '))
d=int(input('Broj osvojenih poena drugog takmicara iz programiranja: '))

x=a+b  #Ukupan broj poena prvog takmicara
y=c+d  #Ukupan broj poena drugog takmicara

if x>y:
    print(1)
elif x<y:
    print(2)
elif x==y:
    if b>d:
        print(1)
    elif b<d:
        print(2)
    else:
        print(1)

