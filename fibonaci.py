
n = int(input ("Koliko Fibonačijevih brojeva treba štampati: "))
br1 = 1
br2 =1
print (br1, br2, end=' ')

for i in range(3,n+1):
    br = br1+br2
    print (br, end = ' ')
    br1,br2 = br2, br
input ()



