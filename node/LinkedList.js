class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    head = null;
    tail = null;

    insert(value) {
        if (this.head === null) {
            this.head = new Node(value);
            this.tail = this.head;
            return;
        }
        let newNode = new Node(value);
        this.tail.next = newNode;
        this.tail = newNode;
    }

    insert(value) {
        if (this.head === null) {
            this.head = new Node(value);
            this.tail = this.head;
            return;
        }
        let newNode = new Node(value);
        let prevPtr = null;
        let ptr = this.head;
        while (ptr !== null && value > ptr.value) {
            prevPtr = ptr;
            ptr = ptr.next;
        }
        if (prevPtr !== null) {
            prevPtr.next = newNode;
        }
        newNode.next = ptr;
        if (prevPtr === null)
            this.head = newNode;
        if (ptr === null)
            this.tail = newNode;
    }

    printList() {
        let ptr = this.head;
        while (ptr !== null) {
            process.stdout.write(ptr.value.toString());
            ptr = ptr.next;
        }
    }
}

const list = new LinkedList();
list.insert(1);
list.insert(0);
list.insert(3);
list.insert(2);
list.printList();