#Ugao izmedju kazaljki

sati=int(input('Unesite broj sati: '))
minuti=int(input('Unesite broj minuta: '))

#sat svodimo na interval [0, 12)
sati=sati%12

# 1 minut predjen na kazaljki je 6 stepeni
# 1 sat = 60 minuta
# 1 sat predjen na kazaljki je 30 stepeni


#ugao u minutima koji minutna kazaljka zauzima sa polozajem 12h
minutnica= minuti*6*60

#ugao u minutima koji satna kazalja zauzima sa polozajem 12h
satnica=sati*30*60 + minuti*30

# ugao izmedju satne i minutne kazaljke u minutima
razlika=abs(minutnica-satnica)


# ugao izmedju kazaljki u stepenima i minutima
ugao_u_stepenima=razlika//60
ugao_u_minutima=razlika%60

#KONACNOOO UGAO IZMEDJU KAZALJKI
print(ugao_u_stepenima,':',ugao_u_minutima)
