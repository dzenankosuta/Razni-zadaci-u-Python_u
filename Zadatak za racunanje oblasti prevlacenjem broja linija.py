'''Zadatak koji racuna koliko disjunktnih oblasti
 dobijemo ako na papiru povucemo n linija'''
def sumi1(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s+1

n=int(input('Unesite broj povlacenja: '))
print('Broj dobijenih oblasti je: ', sumi1(n))
