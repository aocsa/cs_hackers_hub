# %%

class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DLList:
    def __init__(self):
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def insert(self, value):
        ptr = self.head.next
        while ptr != self.tail and ptr.value < value:
            ptr = ptr.next
        new_node = Node(value, ptr.prev, ptr)
        new_node.prev.next = new_node
        new_node.next.prev = new_node

    def print(self, reversed=False):
        ptr = self.tail.prev if reversed else self.head.next
        while ptr != (self.head if reversed else self.tail):
            print(ptr.value, end=' ')
            ptr = ptr.prev if reversed else ptr.next


l = DLList()
l.insert(5)
l.insert(3)
l.insert(4)
l.insert(2)
l.insert(1)
l.insert(6)
print('From head to tail')
l.print()
print('\nFrom tail to head')
l.print(reversed=True)
