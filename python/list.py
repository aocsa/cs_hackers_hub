# %%
class Node: 
    def __init__(self, value):
        self.value = value 
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            return     
        new_node = Node(value)
        self.tail.next = new_node 
        self.tail = new_node

    # [1, 2, 3, 4, 5, 6]
    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            return     

        # step 1: 
        new_node = Node(value)
        # step 2: find new_node position
        prev_ptr = None
        ptr = self.head
        while ptr != None and value > ptr.value:
            prev_ptr = ptr
            ptr = ptr.next
        # step 3: connect everything
        if prev_ptr != None:
            prev_ptr.next = new_node
        new_node.next = ptr
        # step 4: update tail and head
        if prev_ptr == None: # 
            self.head = new_node
        if ptr == None:
            self.tail = new_node  

    def print(self):
        ptr = self.head
        while ptr != None:
            print(ptr.value, end=", ")
            ptr = ptr.next
        print()
    
l = LinkedList()
l.insert(1)
l.print()
l.insert(0)
l.print()
l.insert(3)
l.print()
l.insert(2)
l.print()
