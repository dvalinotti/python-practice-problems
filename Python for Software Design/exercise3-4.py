# Write a function do_twice(f) that takes an argument f (function) and executes it twice.
# Modify do_twice(f) to take another parameter, p that is passed to f when it is executed.
# Then, write a more general version of your test function f that takes a string as a parameter
# and prints it twice.

def print_spam():
    print('spam')

def print_twice( p ):
    for  _ in range(2): print(p)

def do_twice( f, a ):
    for _ in range(2): f(a)

def do_four( f, a ):
    for _ in range(2): do_twice(f, a)
# print_twice('spam')
# do_twice(print_twice, 'spam')
do_four(print_twice, 'spam')