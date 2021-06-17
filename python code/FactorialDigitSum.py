# tim giai thua 
def Factorial(n):
    a=1
    for i in range (1,n+1):
        a=a*i
    return a
# tong chu so
def SumDigit(n):
    a=0
    while (n!=0):
        a=a+n%10
        n=n//10
    return a
n=int(input())
a=Factorial(n)
print (SumDigit(a))