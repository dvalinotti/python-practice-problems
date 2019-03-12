# Take two lists and write a program that returns a list that contains 
# only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

def overlap ( x, y ):
    dupes = []
    l = x
    l.extend(y)
    for i in range( len( l ) ):
        if l[i] in x and l[i] in y:
            dupes.append(l.pop(i))
    return dupes

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print( overlap( a, b ) ) 