#Zadatak za brisanje cifre stotina

n=int(input('Unesite dekadni broj: '))

cifra_s=(n//100)%10

m=(n%100)+100*(n//1000)

print(m)
