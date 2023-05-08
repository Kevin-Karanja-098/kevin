n=int(input('enter a positive nonzero number='))
j=0
for i in range(1,n+1):
      if n%i==0:
          j+=1
          print(i,' ,')
if j==2:
    print ('the number is a prime number')
else:
    print('the number is not a prime number')
print("number has a total of",j,'divisor')      
