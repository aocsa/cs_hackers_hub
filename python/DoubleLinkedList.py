class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.prev = previous

    def insert_asc(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            if self.head.data > data:
                tmp = self.head
                new_node.next = tmp
                self.head = new_node
                tmp.prev = new_node
            else:
                if data > self.tail.data:
                    tmp = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                    self.tail.prev = tmp
                else:
                    current = self.head
                    while current is not None and current.data < data:
                        current = current.next

                    previous_node = current.prev
                    previous_node.next = new_node
                    new_node.prev = previous_node
                    new_node.next = current
                    current.prev = new_node

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
        else:
            if self.tail.data == data:
                previous_node = self.tail.prev
                previous_node.next = None
                self.tail.prev = None
                self.tail = previous_node
            else:
                current = self.head
                while current.next is not None:
                    if current.data == data:
                        previous_node = current.prev
                        next_node = current.next
                        previous_node.next = next_node
                        next_node.prev = previous_node
                        break
                    current = current.next

    def print(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


print('Append to DoubleLinkedList with O(n) as time complexity')
double_linked_list = DoubleLinkedList()
double_linked_list.append(5)
double_linked_list.append(3)
double_linked_list.append(10)
double_linked_list.append(1)
double_linked_list.print()
print('Remove to DoubleLinkedList with O(n) as time complexity')
double_linked_list.remove(10)
double_linked_list.print()

print('Insert to DoubleLinkedList Ascendant with O(n) as time complexity')
another_double_linked_list = DoubleLinkedList()
another_double_linked_list.insert_asc(5)
another_double_linked_list.insert_asc(3)
another_double_linked_list.insert_asc(10)
another_double_linked_list.insert_asc(1)
another_double_linked_list.insert_asc(7)
another_double_linked_list.print()