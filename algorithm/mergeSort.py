def Merge(a,l,r,m):
    t=m-l+1
    p=r-m-1
    L=[0]*t
    R=[0]*p
    for i in range (t):
        L[i]=a[l+i]
    for j in range (p):
        R[j]=a[m+j+1]
    i=0
    j=0
    k=l
    while (i<t and j<p):
        if (L[i]<=R[j]):
            a[k]=L[i]
            i+=1
        else:
            a[k]=R[j]
            j+=1
        k+=1
    while (i<t):
        a[k]=L[i]
        i+=1
        k+=1
    while (j<p):
        a[k]=R[j]
        j+=1
        k+=1
def MergeSort(a,l,r):
    m=(l+r-1)//2
    Merge(a,l,r,m)
    MergeSort(a,l,m)
    MergeSort(a,m+1,r)
    
x=[2,3,4,1,6,5,8,7]
n=len(x)
MergeSort(x,0,n)
for i in range (n):
    print (x[i])
    
            