#Zadatak za mail u toku radnog vremena


a=int(input('Unesite sat prispeca maila: '))
b=int(input('Unesite minut prispeca maila: '))

if a in range(0,25) and b in range(0,60):

    if a in range(9,17):
       print('Dati mail je stigao u toku radnog vremena.')
    else:
       print('Dati mail nije stigao u toku radnog vremena.')
       
else:
    print('Nisu unete korektne vrednosti za sate i minute.')
