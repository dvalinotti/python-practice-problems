# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i. For example, if our input 
# was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], 
# the expected output would be [2, 3, 6]. Follow-up: what if you can't use division?


def arr_multi( arr ):
    result = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for k in range(i-4, i):
            multi = arr[i]
            result[k] *= multi
    return result

print(arr_multi([1, 2, 3, 4, 5]))
print(arr_multi([2, 3, 4, 5, 6]))
print(arr_multi([3, 4, 5, 6, 7]))