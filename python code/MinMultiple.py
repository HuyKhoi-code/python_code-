import math
# tim so mu lon nhat 
def MaxExponential(i,n):
    a=1
    t=i
    while (a<n):
        a=a*i
    return a//t
# tim so nguyen to
def SNT(n):
    if (n<2):
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True
n=10
a=1
for i in range (1,n):
    if (SNT(i)==True):
        a=a*MaxExponential(i,n)
print (a)

