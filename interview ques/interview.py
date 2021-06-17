arr = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
n = len(arr)
count = 0
i = 0
while (i<n):
  if (arr[i] == 0):
    arr.pop(i)
    count += 1
    n -= 1
    i -= 1
  i += 1  
for j in range (count):
    arr.append(0)
print (arr)