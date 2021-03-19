
class Node:
    def __init__(self, k = None, v = None):
        self.key = k
        self.value = v
        self.next = None
        self.prev = None
 

class List: 
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def insert_between(self, prev, new_node, curr):
        prev.next = new_node
        curr.prev = new_node
        new_node.next = curr
        new_node.prev = prev
        self.count += 1

    def push_front(self, node):
        self.insert_between(self.head, node, self.head.next)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.count -= 1
        return node

    def remove_last(self):
        return self.remove(self.tail.prev)

    def first(self):
        return self.head.next

    def last(self):

        
        return self.tail.prev

    def to_string(self):
        output = ""
        curr = self.head.next
        while curr != self.tail :
            output += "(" +  str(curr.key) + " -> " +  str(curr.value) + "), "
            curr = curr.next
        return output

#  diccionary<key, value>
class LRUCache:
    def __init__(self, size):
        self.size = size
        self.dicc = {} # <key, Node>
        self.heap = List()

    def insertKeyValuePair(self, k, v):
        if len(self.dicc) < self.size:
            current_node = Node(k, v)
            self.heap.push_front(current_node)
            self.dicc[k] = current_node
        else:
            # len(self.dicc) == self.size:
            current_node = Node(k, v)
            self.heap.push_front(current_node)

            self.dicc[k] = current_node
            old_node = self.heap.remove_last() # O(1)
            self.dicc.pop(old_node.key)

    def getMostRecentKey(self):
        if self.heap.first():
            return self.heap.first().key
        return None

    def getValueFromKey(self, k):
        if k in self.dicc:
            # TODO: update heap order
            node_to_remove = self.dicc[k] # O(1)
            self.heap.remove(node_to_remove) # O(1)
            node = Node(self.dicc[k].key, self.dicc[k].value)
            self.heap.push_front(node) # O(1)
            return node.value
        return None

# runtime O(1)
# space O(3) -> O(1)
# // All operations below are performed sequentially.
cache = LRUCache(3) # // instantiate an LRUCache of size 3
cache.insertKeyValuePair("b", 2) #: -
cache.insertKeyValuePair("a", 1) #: -
cache.insertKeyValuePair("c", 3) #: -

print(cache.getMostRecentKey()) #: "c" // "c" was the most recently inserted key

print(cache.getValueFromKey("a")) #: 1
print(cache.getMostRecentKey())# "a" // "a" was the most recently retrieved key

cache.insertKeyValuePair("d", 4) #: - // the cache had 3 entries; the least recently
print(cache.getValueFromKey("b")) #: None // "b" was evicted in the previous operation
cache.insertKeyValuePair("a", 5) # - // "a" already exists in the cache so its valu

print(cache.getValueFromKey("a")) # : 5
