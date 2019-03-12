# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
import math

def calc ( d ):
    results = []
    for i in d:
        results.append(int(round(math.sqrt((2 * 50 * i) / 30))))
    return results

print(calc((100, 150, 180)))
