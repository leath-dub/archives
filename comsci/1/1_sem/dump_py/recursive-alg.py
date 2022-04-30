#!/usr/bin/env python3


# defining functions to be used

def quicksort(left, right, array):
    if left >= right:
        return 
    pivot = array[(left + right) // 2]
    # return left from the partition becomes the new pivot
    return_index = partition(left, right, array, pivot)
    # operate on the 2 new sub arrays
    quicksort(left, return_index - 1, array) 
    quicksort(return_index, right, array)

def partition(left, right, array, pivot):
    while left <= right:
        while array[left] > pivot:
            left += 1
        while array[right] < pivot:
            right -= 1
        if left <= right:
            # swap the elements 
            tmp = array[left]
            array[left] = array[right]
            array[right] = tmp
            left += 1
            right -= 1
    return left

# input space diveded numbers
n = int(input())
s = input().split()
# convert array of str nums to ints
array = [int(i) for i in s]
# Define the starting points for algorithm
left = 0
right = n - 1
quicksort(left, right, array)
# builds array from indexs under "if i % 3 == 2" cond
array = [val for i, val in enumerate(array) if i % 3 == 2]
print(sum(array))
