# Count the 2’s between 0 and N. And every 2 digit counts as a 2, so if N was 
# 7 the answer would be 1 (just the number 2), whereas if n was 23 there would 
# be 7 2’s {2, 12, 20, 21, 22 (this counts for 2), 23}. 

def num_of_n ( x, n ):
    count = 0 
    if x == n:
        count += 1
    else:
        for i in range(x + 1):
            if x >= 10:
                numstr = str(i)
                if str(n) in numstr:
                    count += 1
            elif i == n:
                count += 1


    return count

print( num_of_n( 23, 2 ))
print( num_of_n( 7, 2 ))
print( num_of_n( 156, 2 ))
print( num_of_n( 19, 2 ))