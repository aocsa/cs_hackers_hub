class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    fast = head
    slow = head
    while slow != None and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True 
    return False

def get_length(seed):
    ptr = seed.next
    L = 1
    while ptr != seed:
        ptr = ptr.next
        L += 1 
    return L


def find_start(head, length):
    ptr1 = head
    ptr2 = head
    for i in range(length):
        ptr1 = ptr1.next

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next 
    return ptr1.value

def find_duplicate(head): 
    fast = head
    slow = head
    while slow != None and fast.next:
        slow = slow.next # slow = A[slow]
        fast = fast.next.next # fast = A[ A[fast] ]
        if slow == fast:
            L = get_length(slow)
            break 
    if L == 0:
        return -1 
    return find_start(head, L)

def main(): 
    head = Node(2)
    head.next = Node(1)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next

    print(find_duplicate(head))
main()

