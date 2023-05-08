def check_if_fibbonacci(x):
    n = 0
    while n >=0:
        fib=fibbo(n)
        if fib>=x:
            break
        n +=1
    if fib == x:
        return True
    else:
        return False

def fibbo(n):
    if n==1 or n ==0:
        return n
    else:
        return fibbo(n-1)+fibbo(n-2)

def check_if_fibs_neighbour(x,y):
        b = abs(x-y)
        if b<x and b<y:
            print(str(x)+ ' and ' +str(y)+' are neighbouring fibonacci numbers')
        elif b==1:
            print(str(x)+ ' and ' +str(y)+' are neighbouring fibonacci numbers')
        else:
            print(str(x)+ ' and ' +str(y)+' are not neighbouring fibonacci numbers')

x = int (input('enter number'))
y = int(input('enter another number'))
if check_if_fibbonacci(x) == True and check_if_fibbonacci(y) == True:
    check_if_fibs_neighbour(x,y)
elif check_if_fibbonacci(x) == True and check_if_fibbonacci(y) == False:
    print(str(x)+' is a fibonacci number' + ' but ' +str(y)+' is not')
elif check_if_fibbonacci(y) == True and check_if_fibbonacci(x) == False:
    print(str(y)+' is a fibonacci number' + ' but ' +str(x)+' is not')
else:
    print(str(x)+' and ' +str(y)+' are not fibonacci numbers')
