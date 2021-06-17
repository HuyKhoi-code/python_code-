# tim uoc cua so n
import math 
def SumOfDevisior(n):
    t=1
    for i in range (2,int(math.sqrt(n))+1):
        if (n%i==0):
            t=i+n//i+t
    return t
n=10000
t=0
k=0
for i in range (1,n):
    j=SumOfDevisior(i)
    if (SumOfDevisior(j)==i and i!=j and j!=t):
        t=i
        k=k+i+j
print (k)



