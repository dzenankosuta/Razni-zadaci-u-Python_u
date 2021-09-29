
a=str(input('Unesite niz: '))
b=str(input('Unesite podniz prethodno unetog niza: '))

def skracivanje(a,b):
    for i in a:
        a=a.replace(b,'')
    return a
print(skracivanje(a,b))


