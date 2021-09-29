#broj sekundi pretvoren u stepene,minute,sekunde

brsek=int(input('Unesite broj sekundi koji zelite pretvoriti \
u stepene, minute i sekunde: '))

step=brsek//3600            #BROJ CELIH STEPENI
minu=((brsek%3600)//60)     #BROJ MINUTA
sek=(brsek%3600)%60         #BROJ SEKUNDI

print(f"Broj ukupnih stepeni je: {step}")
print(f"Broj ukupnih minuta je: {minu}")
print(f"Broj ukupnih sekundi je: {sek}")
