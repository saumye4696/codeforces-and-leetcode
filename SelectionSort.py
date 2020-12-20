def selection(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i+1,len(arr)):
            if(arr[j] < arr[small]):
                small = j
        arr[small] , arr[i] = arr[i] , arr[small]
    return arr

l1 = [2,3,9,8,7,5,3,7,8]
print(selection(l1))