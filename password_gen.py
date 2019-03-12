# Write a password generator in Python. Be creative with how you generate 
# passwords - strong passwords have a mix of lowercase letters, uppercase 
# letters, numbers, and symbols. The passwords should be random, generating a 
# new password every time the user asks for a new password. 

import random

def generate_password( cplx ):
    result = ""
    low = "abcdefghijklmnopqrstuvwxyz"
    medium = low + "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    high = medium + "!@#$%^&*()_+=-?!"
    if ( cplx == "low" ):
        result = random.sample(low, 8)
    elif ( cplx == "medium" ):
        result = random.sample(medium, 16)
    else:
        result = random.sample(high, 24)
    return ''.join(result)

print(generate_password("low"))
print(generate_password("medium"))
print(generate_password("high"))

