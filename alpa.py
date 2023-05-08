a='abcdefghijklmnopqwrstuvwxyz'
##b = str()
m=len(a)
##j=0
##while j<m:
##    b=a[j:m]+a[0:j]
##    j=j+1
##    print(b)
for j in range(m):
    b = a[j:m] + a[0:j]
    print(b)
