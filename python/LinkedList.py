class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        current = self.head
        if self.head is None:
            self.head = Node(data)
            return self.head
        else:
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node

    def insert_asc(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            if self.head.data > new_node.data:
                new_node.next = self.head
                self.head = new_node
            else:
                if data > self.tail.data:
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    current = self.head
                    while current.next is not None and current.next.data < data:
                        current = current.next
                    next_node = current.next
                    current.next = new_node
                    new_node.next = next_node

    def remove(self, data):
        current = self.head
        if self.head.data == data:
            self.head = self.head.next
        else:
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    break
                current = current.next

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


print('Append to LinkedList with O(n) as time complexity')
linked_list = LinkedList()
linked_list.append(5)
linked_list.append(3)
linked_list.append(10)
linked_list.append(1)
linked_list.print()
print('Remove to LinkedList with O(n) as time complexity')
linked_list.remove(10)
linked_list.print()

print('Insert to LinkedList with O(1) as time complexity')
another_linked_list = LinkedList()
another_linked_list.insert(5)
another_linked_list.insert(3)
another_linked_list.insert(10)
another_linked_list.insert(1)
another_linked_list.print()

print('Insert to LinkedList Ascendant with O(n) as time complexity')
last_linked_list = LinkedList()
last_linked_list.insert_asc(5)
last_linked_list.insert_asc(3)
last_linked_list.insert_asc(10)
last_linked_list.insert_asc(1)
last_linked_list.print()
