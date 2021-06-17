q=int(input())
arr=[]
b=[]
for i in range (q):
    s=input()
    t=input()
    arr.append(s)
    b.append(t)
def checkSimilar(x,y):
    count=0
    for i in range (len(x)):
        for j in range (i-1,i+1):
            if (x[i])==(y[j]):
                if (i==j):
                    count+=2
                    i+=1
                    continue
                count+=1
                continue
            else:
                if (x[i-1]==y[j]):
                    count+=1
                    continue
    return count
for i in range (q):
    if (checkSimilar(arr[i],b[i])>=len(arr[i])-1):
        print (checkSimilar(arr[i],b[i]))
        print ("YES")    
    else:
        print ("NO") 
