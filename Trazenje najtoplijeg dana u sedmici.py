#Trazenje najtoplijeg dana u sedmici

lista=[]

for i in range(7):
    x=int(input('Unesite temperatutu %i. dana u sedmici:' %(i+1)))
    lista.append(x)

for i in range(len(lista)):
    if lista[i]==max(lista):
        print(i+1)
        break
