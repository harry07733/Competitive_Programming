"""A rotated array is an array with its elements being shifted towards left or right by a 'some number' of indices. For example, if the array = {1, 2, 3, 4, 5} and if it is rotated right by two indices, the resultant array = {4, 5, 1, 2, 3}.Given an array A of N elements, A is sorted in increasing order and is rotated some number of times unknown to you beforehand. Write a program to find the smallest and the largest element of A."""

def getPivotElement(num_list, n, start, end):
    if(num_list[start] < num_list[end]):
        return start, end
    mid = (start + end) // 2
    if(mid < n - 1 and num_list[mid] < num_list[mid + 1] and num_list[mid] < num_list[mid - 1]):
        return mid, mid - 1
    if(mid < n - 1 and num_list[mid] > num_list[mid+1]):
        return mid + 1 , mid 
    if(num_list[mid] < num_list[end]):
        return getPivotElement(num_list, n, start, mid)
    else:
        return getPivotElement(num_list, n, mid + 1, end)
    
size = int(input())
num_list = list(map(int, input().split()))

pivot, last_index = getPivotElement(num_list, size, 0, size - 1)
print(num_list[pivot], end = " ")
print(num_list[last_index])