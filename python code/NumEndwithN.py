n,m=input().split()
t=m[:-len(n)]
p=m[len(t):]
a=0
a+=int(t)
if (int(p)>=int(t)):
    a+=1
print (a)