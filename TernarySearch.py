def ternary(arr, k, l ,r):
    mid1 = int(l + (r-l)/3)
    mid2 = int(r - (r-l)/3)
    while(r >= l):
        if(arr[mid1] == k):
            return mid1
        if(arr[mid2] == k):
            return mid2
        if(k < arr[mid1]):
            r = mid1 - 1
            mid1 = int(l + (r-l)/3)
        elif(k > arr[mid2]):
            l = mid2 + 1
            mid2 = int(r - (r-l)/3)
        else:
            l = mid1 + 1
            r = mid2 - 1
            mid1 = int(l + (r-l)/3)
            mid2 = int(r - (r-l)/3)
    return -1

l1 = [2,3,5,6,8,9,12,13,18]
if(ternary(l1, 19, 0 ,len(l1)-1) == -1):
    print("NOT FOUND")
else:
    print("FOUND")  