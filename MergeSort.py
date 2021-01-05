# Refer python alternative code from geeksforgeeks 

def mergeSort(arr):
    
    if(len(arr) > 1):
        m = len(arr)//2
        left = arr[:m]
        right = arr[m:]
        mergeSort(left)
        mergeSort(right)

        final = []

        while len(left) > 0 and len(right) > 0 :
            if(left[0] > right[0]):
                final.append(left[0])
                left.pop(0)
            else:
                final.append(right[0])
                right.pop(0)
                
        for i in left:
            final.append(i)
        for i in right:
            final.append(i)
        
    return final

l1 = [12, 11 , 13, 4,5 ,6,2]
a = mergeSort(l1)
print(*a)