#pretvara listu u string(ali mora biti svaki element liste string)
a=['a','bv']
s=''

for i in range(len(a)):
    s=s+a[i]
    
print(s)

#vraca prvi element liste

a=['a','bv']
s=''

for i in a:
    s=i
    break
print(s)

#vraca prvi element stringa 1.nacin

x='abc'
y=''

for i in range(len(x)):
    y=y+x[i]
    break
print(y)

#vraca prvi element stringa 2.nacin

x='abc'


for i in x:
    y=i
    break
print(y)


