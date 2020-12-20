def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) -i - 1):
            if(arr[j] > arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1], arr[j]
    return arr
    # after every iteration, the next largest number will
    # be sent to the end in its correct position
    
l1 = [9,6,4,3,6,4,3,6,7,9,2,1,6,7,8]
l2 = []
l2 = bubble(l1)
print(l2)