def check (n):
    arr = []
    while (n != 0):
        arr.append (n % 10)
        n = n//10
    for i in range (len(arr)):
        if (arr[i] != arr[n-i-1]):
            return False
    return True

n = 143341
print (check(n))
