#Polja na sahovskoj tabli

n=int(input('Unesite sirinu table:'))
m=int(input('Unesite duzinu table:'))

polja=n*m
crne=0

for i in range(2,polja+1,2):
    crne+=1

print(crne)
