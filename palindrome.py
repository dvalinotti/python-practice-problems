# Ask the user for a string and print out whether this string is a palindrome 
# or not. (A palindrome is a string that reads the same forwards and backwards.)

def is_palindrome ( s ):
    i = 0
    n = -1
    while (i < len(s)):
        if (s[i] != s[n]):
            return False
        i += 1
        n -= 1
    return True

print( is_palindrome("daniel") )