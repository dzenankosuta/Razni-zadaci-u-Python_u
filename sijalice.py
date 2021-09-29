#Sijalice

h1,m1,s1=input().split()
h2,m2,s2=input().split()
h3,m3,s3=input().split()
h4,m4,s4=input().split()

h1=int(h1)
h2=int(h2)
h3=int(h3)
h4=int(h4)
m1=int(m1)
m2=int(m2)
m3=int(m3)
m4=int(m4)
s1=int(s1)
s2=int(s2)
s3=int(s3)
s4=int(s4)


pp=h1*3600+m1*60+s1
kp=h2*3600+m2*60+s2
pz=h3*3600+m3*60+s3
kz=h4*3600+m4*60+s4


a=[pp,kp,pz,kz]
a.sort()

#pltrh=plt//3600         KOLIKO SATI JE TRAJALO PLAVO OSVETLJENJE
#pltrm=(plt%3600)//60    KOLIKO MINUTA
#pltrs=(plt%3600)%60     KOLIKO SEKUNDI

#zutrh=zut//3600         KOLIKO SATI JE TRAJALO ZUTO OSVETLJENJE
#pltrm=(zut%3600)//60    KOLIKO MINUTA
#pltrs=(zut%3600)%60     KOLIKO SEKUNDI

#zetrh=zet//3600         KOLIKO SATI JE TRAJALO ZELENO OSVETLJENJE
#pltrm=(zet%3600)//60    KOLIKO MINUTA
#pltrs=(zet%3600)%60     KOLIKO SEKUNDI

if a[0]==pp:
    if a[1]==kp:
        plt=a[1]-a[0]
        print(plt//3600, ':',(plt%3600)//60, ':', (plt%3600)%60 )
        zut=a[3]-a[2]
        print(zut//3600, ':',(zut%3600)//60, ':', (zut%3600)%60 )
        zet=0
        print(zet//3600, ':',(zet%3600)//60, ':', (zet%3600)%60 )
    elif a[1]==pz and a[2]==kp:
        plt=a[1]-a[0]
        print(plt//3600, ':',(plt%3600)//60, ':', (plt%3600)%60 )
        zut=a[3]-a[2]
        print(zut//3600, ':',(zut%3600)//60, ':', (zut%3600)%60 )
        zet=a[2]-a[1]
        print(zet//3600, ':',(zet%3600)//60, ':', (zet%3600)%60 )
    elif a[1]==pz and a[2]==kz:
        plt=a[1]-a[0]+a[3]-a[2]
        print(plt//3600, ':',(plt%3600)//60, ':', (plt%3600)%60 )
        zut=0
        print(zut//3600, ':',(zut%3600)//60, ':', (zut%3600)%60 )
        zet=a[2]-a[1]
        print(zet//3600, ':',(zet%3600)//60, ':', (zet%3600)%60 )

elif a[0]==pz:
    if a[1]==kz:
        plt=a[3]-a[2]
        print(plt//3600, ':',(plt%3600)//60, ':', (plt%3600)%60 )
        zut=a[1]-a[0]
        print(zut//3600, ':',(zut%3600)//60, ':', (zut%3600)%60 )
        zet=0
        print(zet//3600, ':',(zet%3600)//60, ':', (zet%3600)%60 )
    elif a[1]==pp and a[2]==kz:
        plt=a[3]-a[2]
        print(plt//3600, ':',(plt%3600)//60, ':', (plt%3600)%60 )
        zut=a[1]-a[0]
        print(zut//3600, ':',(zut%3600)//60, ':', (zut%3600)%60 )
        zet=a[2]-a[1]
        print(zet//3600, ':',(zet%3600)//60, ':', (zet%3600)%60 )
    elif a[1]==pp and a[2]==kp:
        plt=0
        print(plt//3600, ':',(plt%3600)//60, ':', (plt%3600)%60 )
        zut=a[1]-a[0]+a[3]-a[2]
        print(zut//3600, ':',(zut%3600)//60, ':', (zut%3600)%60 )
        zet=a[2]-a[1]
        print(zet//3600, ':',(zet%3600)//60, ':', (zet%3600)%60 )



