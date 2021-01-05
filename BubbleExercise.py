def bubble(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr) -i - 1):
            if(arr[j] > arr[j+1]):
                arr[j] , arr[j+1] = arr[j+1], arr[j]
                count += 1
    return count

n = int(input())
l1 = []
l1 = list(map(int,input().split()))
print(bubble(l1))