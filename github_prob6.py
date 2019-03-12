# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i * j.

def calc( x, y ):
    result = [[],[],[]]
    for i in range(x):
        for j in range(y):
            result[i].append( i * j )
    return result

def print_2d ( arr ):
    for i in range(len(arr)):
        print(arr[i])

print_2d(calc(3, 5))
