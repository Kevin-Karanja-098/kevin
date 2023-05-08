a=[21,22,10,17,19,18,655,77,24,67,80,23,46]
print(a)
for i in range (len(a)):
        if a[i]%2==0:
                for k in range (len(a)):
                        if a[k]<a[i] and a[k]%2==0:
                                a[k],a[i]=a[i],a[k]
print (a)
a[1]=78
print(a)









