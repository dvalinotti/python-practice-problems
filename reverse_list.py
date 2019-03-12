# Find a quick way to reverse a list.

def reverse_list ( l ):
    new = []
    i = len(l) - 1
    while len(new) < i:
        new.append(l.pop(i))
        i = i - 1
    return new

b = [1, 5, 7, 12, 13, 19, 21]
print( reverse_list( b ) )