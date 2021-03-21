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
        current = self.head.next
        while current != self.tail and current.value < value:
            current = current.next
        new_node = Node(value, current.prev, current)
        new_node.prev.next = new_node
        new_node.next.prev = new_node

    def print(self):
        current = self.head.next
        while current != self.tail:
            print(current.value, ' ')
            current = current.next


l = DLList()
l.insert(5)
l.insert(3)
l.insert(4)
l.insert(2)
l.insert(1)
l.insert(6)
l.print()

# %%
