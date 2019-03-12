# Write a program which can compute the factorial of a given numbers.The results should be printed 
# in a comma-separated sequence on a single line.Suppose the following input is supplied to the 
# program: 8 Then, the output should be:40320

def fact_recursive( x ):
    if x == 0: 
        return 1
    return x * fact(x-1)

def fact( x ):
    result = 1
    if x == 0:
        return 1
    for i in range(x):
        result *= i+1
    return result

print(fact(4))
print(fact(5))
print(fact(8))

print(fact_recursive(4))
print(fact_recursive(5))
print(fact_recursive(8))
