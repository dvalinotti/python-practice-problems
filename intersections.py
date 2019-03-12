# Given two different lists of objects, come up with an efficient solution to find 
# the intersection of the two lists

def find_intersection ( arr1, arr2 ):
    inter = []
    if ( len( arr1 ) >= len( arr2 ) ):
        for i in range(len(arr1)):
            find = arr1[i]
            if (find in arr2):
                inter.append( ( i, arr2.index(find)) )
    else:
        for i in range(len(arr2)):
            find = arr2[i]
            if (find in arr1):
                inter.append( ( i, arr1.index(find)) )
    return inter

arr1 = [1, 3, 5, 7, 9, 12]
arr2 = [3, 6, 9, 12]

print(find_intersection(arr1, arr2))