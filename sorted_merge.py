# We have two sorted lists, and we want to write a function to merge the two
# lists into one sorted list
def sort ( a , b ):
    a.extend(b)
    return sorted(a)

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]

print(sort(a, b))