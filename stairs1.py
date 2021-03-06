# Problem: Given n, a number of stairs, calculate the number of ways you can climb the stairs if you can climb
#   one (1) or two (2) stairs at a time.

def num_ways( n ):
    total = 0
    if (n == 0 or n - 1 == 0):
        total = 1
    elif ( n - 1 >= 0 ):
        total += num_ways( n - 1 )
        if ( n - 2 >= 0 ):
            total += num_ways ( n - 2 )
    return total
    

print (num_ways(1))
print (num_ways(2))
print (num_ways(3))
print (num_ways(4))
