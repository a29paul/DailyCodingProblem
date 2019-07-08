# This problem was asked by Google.

# A unival tree(which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.



class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree1 = Node(1,1,1)
tree2 = Node(1,Node(1,Node(1,1,2),1))
def is_unival(node):
    if type(node) == int:
        return True
    if node.left == None and node.right == None:
        return True
    if type(node.left) == int and type(node.right) == int:
        if node.val == node.right and node.val == node.left:
            return True
    elif type(node.right) != int and type(node.left) != int:
        if node.val == node.right.val and node.val == node.left.val:
            return True
    elif type(node.left) != int:
        if node.val == node.left.val and node.val == node.right:
            return True
    elif type(node.right) != int:
        if node.val == node.right.val and node.val == node.left:
            return True
    return False

# Come back to this later!!

print(tree1.right.val)
