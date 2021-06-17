a,b=[int(a) for a in input().split()]
x=list(map(int,input().split()))
y=list(map(int,input().split()))
t=[]
for i in range (a):
    t.append(x[i])
for i in range (b):
    t.append(y[i])
t.sort()
print (t)
