
# %%
class Node: 
    def __init__(self, value = 0):
        self.value = value
        self.height = 0
        self.children = [None, None]

class GNode: 
    def __init__(self, value, children):
        self.value = value
        self.children = children

# DFS
# BT(t) = (BT(t.left) | t | BT(t.right)) # inorder -> sort
# BT(t) = (| t | BT(t.left) BT(t.right)) # preorder -> 
# BT(t) = (BT(t.left) BT(t.right) | t |) # postorder -> 

# BFS

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

def DFS(start_node):
    result = []
    visited = {}
    stack = [start_node]
    while len(stack) > 0:
        node = stack.pop(len(stack) - 1)
        if node.value in visited:
            continue
        visited[node.value] = True 
        result.append(node.value)
        for index in range(len(node.children) - 1, -1, -1):
            if node.children[index] is not None:
                stack.append(node.children[index])
    print(result)

def BFS(start_node):
    result = []
    visited = {}
    queue = [start_node]
    while len(queue) > 0:
        node = queue.pop(0)
        if node.value in visited:
            continue
        visited[node.value] = True        
        result.append(node.value)
        for index in range(0, len(node.children)):
            if node.children[index] is not None:
                queue.append(node.children[index])
    print(result)

b = BinaryTree()
b.insert(5)
b.insert(3)
b.insert(2)
b.insert(4)
b.insert(7)
b.insert(6)
b.insert(8)
b.print()

# g = GNode()

DFS(b.root)
BFS(b.root)

# %%
