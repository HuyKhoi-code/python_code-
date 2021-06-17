n=14247
p1=n
p2=n
if (n%10==0):
    exit(1)
sum=1
while (p1!=0):
    sum=sum*10
    p1=p1//10
sum=sum//10
a=[]
while (p2!=0):
    t=p2//sum
    p2=p2%sum
    sum=sum//10
    a.append(t)
b=len(a)
tong=0
c=0
for i in range (b):
    c+=a[i]
if (c//b==9):
    tong=n+2
else:
    a[b-1]=a[0]
    if (b%2==0):
        for i in range (1,b//2):
            while (a[i]!=a[b-i-1]):
                if (a[i]<=a[b-i-1]):
                    a[i]+=1
                    a[b-i-1]=a[i]
                else:
                    a[b-i-1]=a[i]
    elif (b%2!=0 and b>3):
        for i in range (1,b//2+1):
            if (a[i]<=a[b-i-1]):
                a[i]+=1
                a[b-i-1]=a[i]
            else:
                a[b-i-1]=a[i]
    elif(b==3):
        a[1]+=1
    for i in range (b):
        tong=tong*10+a[i]
print(tong)



