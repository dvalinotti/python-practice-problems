count = 0

def subsets ( arr ):
    subset = []
    for i in range( len( arr ) ):
        subset.append( None )
    subsets_helper( arr, subset, 0 )
    return count

def subsets_helper ( arr, subset, i ):
    if i == len( arr ):
        global count
        count += 1
        print ( subset )
    else:
        subset[i] = None
        subsets_helper( arr, subset, i+1 )
        subset[i] = arr[i]
        subsets_helper( arr, subset, i+1 )

    
sub = [1, 2]
c = subsets( sub )
print "There are ", c, " subsets of ", sub 