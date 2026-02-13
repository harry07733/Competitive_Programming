def get_the_index(arr, n, k):
    start = 0
    end = n - 1
    while(start <= end):
        mid = (start + end) // 2
        if(arr[mid] == k):
            return mid
        elif(arr[mid] < k):
            start = mid + 1 
        else:
            end = mid - 1
    return "Element not inside the sequence"

size = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
item = int(input())                           ## The item to be found in the list

index = get_the_index(num_list, size, item)
print(index)