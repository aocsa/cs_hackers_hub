struct Node {
    value: i32,
    next: Option<Box<Node>> 
}

struct LinkedList {
    head: Option<Box<Node>>,
    tail: Option<*mut Node>
}

impl LinkedList {
    fn new() -> Self {
        LinkedList{
            head: None,
            tail: None
        }
    }
    fn push_back(&mut self, value: i32) {
        let mut new_tail = Box::new(Node { value, next: None });
        let raw_tail: *mut _ = &mut *new_tail;

        if self.tail.is_some() {
            unsafe { (*self.tail.unwrap()).next = Some(new_tail) };
        } else {
            self.head = Some(new_tail);
        }
        self.tail = Some(raw_tail);
    }

    pub fn pop_back(&mut self) -> Option<i32> {
        if let Some(head) = &mut self.head {
            let old_value = Some(head.value);
            let new_head = head.next.take();
            if new_head.is_none() {
                self.tail = None;
            };
            self.head = new_head;
            old_value
        } else {
            None
        }
    }
    fn print(&mut self) {
        let mut node  = &self.head;
        while let Some(old_node) = node  {
            match &node {
                Some(node) => print!("{}", node.value),
                _ => () ,
            }
            node = &old_node.next;
        }
        println!("")
    }
}

fn main() {
    let mut list = LinkedList::new();
    list.push_back(0);
    list.push_back(1);
    list.push_back(2);
    list.push_back(3);
    list.print();
}