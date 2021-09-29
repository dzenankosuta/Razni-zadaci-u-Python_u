#Razmaknute dijagonale na sahovskoj tabli

x,y=input().split()

x=int(x)
y=int(y)

if (x+y)%3==1:
    print('crno')
else:
    print('belo')
