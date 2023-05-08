def power_of_2(n):
    if n==1:
        return True
    elif n>1:
        return power_of_2(n/2)
    else:
        return False
n=int(input('enter a number'))
if power_of_2(n)==True:
    print("the number above is a power of 2")
else:
    print("the number above is not a power of 2")
