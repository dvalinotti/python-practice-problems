# Write a program (using functions!) that asks the user for a long string 
# containing multiple words. Print back to the user the same string, except 
# with the words in backwards order.

def reverse ( s ):
    words = s.split()
    return [words[-i - 1] for i in range(len(words))]

print(reverse("Hello world and all who inhabit it"))