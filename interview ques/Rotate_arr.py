def Rotate (arr, i, j):
    x = 0 
    while x <= (j-i)//2:
        arr[i + x], arr[j-x] = arr[j-x], arr[i+x]
        x += 1
    return arr

def Rotate_by_k(arr, k):
    n = len (arr)
    Rotate(arr, 0, n-1)
    Rotate(arr, 0, k)
    Rotate(arr, k+1, n-1)
    return arr
arr = [1, 2 ,3, 4, 5, 6, 7]
print (Rotate_by_k(arr, 3))

