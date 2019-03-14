# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def serialize(root):
    return encode(root)
def encode (node):
    result = ""
    if node:
        result += node.val + " "
        encode(node.left)
        encode(node.right)
    else:
        result += "None "
    return result
def deserialize(s):

    return 0

node = Node('root', Node('left', Node('left.left')), Node('right'))
node1 = Node('1', Node('2'), Node('3', Node('4'), Node('5')))
print(serialize(node1))
print(deserialize(serialize(node)))