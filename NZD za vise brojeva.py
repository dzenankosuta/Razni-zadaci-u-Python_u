

lista=[8,4,16]



def nzd(lista):
    nzd=1
    for i in range(2,min(lista)+1):
        if lista[0]%i==0 and lista[1]%i==0 and lista[2]%i==0:
            nzd=i
    return nzd 


print(nzd(lista))
