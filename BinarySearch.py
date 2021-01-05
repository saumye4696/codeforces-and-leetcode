def binary(arr, k):
    # k is the element to be searched
    low = 0
    high = len(arr)
    mid = int((low + high)/2)
    while(low <= high):
        if(k == arr[mid]):
            print("index : ",mid)
            return True
        elif(k < arr[mid]):
            high = mid - 1
        elif(k > arr[mid]):
            low = mid + 1
        mid = int((low + high)/2)
    return False

l1 = [1,2,3,4,4,5,6,7,7,8,9]
if(binary(l1 , 4)):
    print("FOUND")
else:
    print("NOT FOUND")