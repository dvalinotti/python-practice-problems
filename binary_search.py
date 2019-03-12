# Write a function that takes an ordered list of numbers (a list where the elements are in order 
# from smallest to largest) and another number. The function decides whether or not the given 
# number is inside the list and returns (then prints) an appropriate boolean.

def search( n, k, l=0, h=None):
    if h is None:
        h = len(n) - 1
    if l > h:
        return False

    m = (l + h) // 2
    if (n[m] == k):
        return True
    else:
        if n[m] > k:
            return search( n, k, l, m-1 )
        if n[m] < k:
            return search( n, k, m+1, h)
    

nums = [1, 3, 4, 5, 6, 7, 10, 11, 12, 13, 18, 19, 21]

print(search(nums, 9))
print(search(nums, 5))
print(search(nums, 12))
print(search(nums, 14))
print(search(nums, 27))