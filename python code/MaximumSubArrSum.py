# max arr if arr[mid] in it
def MaxCrossing(arr,l,m,r):
    #element on the left side
    sm=0
    SumLeft=-1000
    for i in range (m,l-1,-1):
        sm+=arr[i]
        if (sm>SumLeft):
            SumLeft=sm
    # elements on the right side
    sm=0
    SumRight=-1000
    for i in range (m-1,r+1):
        sm+=arr[i]
        if (sm>SumRight):
            SumRight=sm
    return SumLeft+SumRight
# return the max sum of the sub arr
def MaxSubArrSum(arr,l,r):
    if (l==r):
        return arr[l]
    else:
        m=(l+r)//2
        return max(MaxSubArrSum(arr,0,m), MaxSubArrSum(arr,m+1,r),MaxCrossing(arr,l,m,r))
arr=[-10,9,-5,6,-8,12,-4,-3]
print (MaxSubArrSum(arr,0,len(arr)-1))