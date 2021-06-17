def ZeroMove(arr):
    n=len(arr)-1
    for i in range (n):
        if (arr[i]==0):
            arr.pop(i)
            arr.append(0)
            n-=1
    return arr
arr=[1,0,2,0,5,74,8,3,6,3,0,4,8,0,6]
print (ZeroMove(arr))