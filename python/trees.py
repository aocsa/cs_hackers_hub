
# %%
class Node: 
    def __init__(self, value = 0):
        self.value = value
        self.height = 0
        self.children = [None, None]

# DFS
# BT(t) = (BT(t.left) | t | BT(t.right)) # inorder -> sort
# BT(t) = (| t | BT(t.left) BT(t.right)) # preorder -> 
# BT(t) = (BT(t.left) BT(t.right) | t |) # postorder -> 

# inorder:  (BT(t.left) | t | BT(t.right))
def inorder(ptr, level):
    if ptr is not None: 
        inorder(ptr.children[0], level + 1)
        print(ptr.value)        
        inorder(ptr.children[1], level + 1)

def recursive_print(ptr, level):
    if ptr is not None: 
        recursive_print(ptr.children[1], level + 1)
        for i in range(level):
            print("....", end="")
        print(ptr.value)        
        recursive_print(ptr.children[0], level + 1)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            pos = 0
            prev = None
            ptr = self.root
            while ptr:
                pos = 0 if value < ptr.value else 1 
                prev = ptr
                ptr = ptr.children[pos]
            prev.children[pos] = new_node
    
    def print(self):
        recursive_print(self.root, 0)
        

b = BinaryTree()
b.insert(5)
b.insert(3)
b.insert(2)
b.insert(4)
b.insert(7)
b.insert(6)
b.insert(8)

b.print()

