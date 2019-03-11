# Problem: Given n, a number of stairs, and x, and array of the number of stairs you can climb per-step,
#   caluclate the number of possible ways to climb the stairs.

def num_ways ( n , x ):
    total = 0
    if ( n == 0 ): 
        return 1
    for i in x :
        if ( n - i >= 0):
            total += num_ways( n - i , x )


    return total



print (num_ways(4, [1, 3, 5]))