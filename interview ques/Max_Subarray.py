def Max_Subarr(arr):
    current_arr = max_arr = arr[0]
    for i in range (1, len(arr) - 1):
        current_arr = max(arr[i],current_arr + arr[i])
        if (current_arr > max_arr):
            max_arr = current_arr
    return max_arr
arr=[1,-2,4,1,3,-5,-7]
print (Max_Subarr(arr))