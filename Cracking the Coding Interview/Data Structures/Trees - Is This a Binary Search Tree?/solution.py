""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def check(root, min, max):
    if root is None:
        return True
    if root.data < max and root.data > min:
        return (check(root.right, root.data, max) and check(root.left, min, root.data))
    return False

def checkBST(root):
    if check(root, 0, 10e4):
        return True
    else:
        return False