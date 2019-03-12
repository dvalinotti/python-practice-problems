# DAILY CODING PROBLEM: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def adds_up_to( l, k, i=0 ):
    if i == len(l):
        return False
    else:
        for item in l:
            if l[i] + item == k:
                return True
            return adds_up_to( l, k, i+1)

nums = [10, 15, 3, 7]
print(adds_up_to( nums, 17 ))
print(adds_up_to( nums, 16 ))