# A number is input in computer then a new no should get printed by adding one to each of its digit. 
# If you encounter a 9, insert a 10 (don't carry over, just shift things around).
import math

def add_to_digits( num ):
    digits = int(math.log10(num)) + 1
    result = num
    for i in range(digits):
        if i == 0:
            result += 1
        else:
            result += 10**i
    return result

print(add_to_digits(5))
print(add_to_digits(901))
print(add_to_digits(99999))