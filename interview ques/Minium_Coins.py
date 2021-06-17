def Minium (arr, k):
    i = 0 
    tong = 0
    n = len(arr) 
    while tong != arr[n-1]:
        j = i + 1
        tong += arr[i]
        if (tong > k):
            tong = arr[j]
            i+=1
        elif (tong == k):
            return arr[j-1:i+1]
        if (j == len(arr) - 1):
            i = j  
        i+=1



arr = [5, 10, 1, 25]
print (Minium(arr, 11))
            
