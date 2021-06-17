import math 
# tim tong uoc 
def SumOfDivisor(n):
    t=0
    for i in range (1,int(math.sqrt(n))+1):
        if (n%i==0):
            t=t+i+n//i
            if (i==n//i):
                t=t-i
    return t-n
# kiem tra so abudant
def CheckAbudant(n):
    if (n<SumOfDivisor(n)):
        return True
    return False
n=int(input())
t=0
for i in range (1,n):
    if (CheckAbudant(i)==True):         
        t=t+i
print (t)

