use std::collections::HashMap;
use std::mem;
use std::boxed::Box;

struct Node {
    key: String,
    value: i32,
    next: Option<*mut Node>,
    prev: Option<*mut Node>
}

struct LinkedList {
    head: Box<Node>,
    tail: Box<Node>,
}
impl LinkedList{
    fn new() -> Self {
        let mut list = LinkedList{
            head: Box::new(Node { key:"".to_string(), value:0, next: None, prev: None }),
            tail: Box::new(Node { key:"".to_string(), value:0, next: None, prev: None }),
        };
        unsafe {
            let mut raw_tail =  &mut *list.tail as *mut Node;
            let mut raw_head =  &mut *list.head as *mut Node;
            list.tail.as_mut().next = Some(raw_head);
            list.head.as_mut().next = Some(raw_tail);
        }
        list
    }

    fn insert(&mut self, new_node: *mut Node, prev:*mut Node, curr:*mut Node ){
        unsafe{
            (*prev).next = Some(new_node);
            (*curr).prev = Some(new_node);
            (*new_node).next = Some(curr);
            (*new_node).prev = Some(prev);
        }
    }

    fn push_front(&mut self, new_node:*mut Node){
        unsafe{
            let mut raw_head = &mut *self.head as *mut Node;
            self.insert(new_node, raw_head, (*raw_head).next.unwrap());
        }
    }

    fn remove(&mut self, ptr:*mut Node ){
        unsafe{
            (*(*ptr).prev.unwrap()).next = (*ptr).next;
            (*(*ptr).next.unwrap()).prev = (*ptr).prev;
        }
    }
    fn remove_last(&mut self) {
        return unsafe{
            let mut last_node = self.tail.as_mut().prev.unwrap();
            self.remove(last_node)
        };
    }

    fn first(&mut self) -> *const Node {
        return unsafe{
            self.head.as_mut().next.unwrap()
        };
    }
    fn last(&mut self) -> *const Node {
        return unsafe{
            self.tail.as_mut().prev.unwrap()
        };
    }

    fn print(&mut self) {
        unsafe {
            let mut raw_head = &mut *self.head as *mut Node;
            let mut ptr = (*raw_head).next.unwrap();
            let mut raw_tail = &mut *self.tail as *mut Node;
            while ptr != raw_tail {
                println!("({}, {}) -> ", (*ptr).key, (*ptr).value);
                ptr = (*ptr).next.unwrap();
            }
            println!();
        }
    }
}

use std::any::type_name;

fn type_of<T>(_: T) -> &'static str {
    type_name::<T>()
}


struct LRUCache {
    heap: LinkedList,
    dicc: HashMap<String, Option<Box<Node>>>,
    size:usize
}

impl LRUCache{
    fn new(size:usize) -> Self {
        LRUCache{
            heap: LinkedList::new(),
            dicc: HashMap::new(),
            size
        }
    }

    fn insert(&mut self, key:String, value:i32){
        let key_cp = key.to_string();
        let mut new_node = Box::new(Node { key:key, value:value, next: None, prev: None });
        let raw_new_node = &mut *new_node as *mut Node;
        let mut result = self.dicc.get_mut(&key_cp);
        if result.is_some() {
            unsafe {
                let mut node_optional = result.as_mut().unwrap();
                let mut node = node_optional.as_mut().unwrap();
                let mut raw_node = node.as_mut();
                raw_node.value = value;
                self.getValueFromKey(key_cp);
            };
        } else {
            if self.dicc.len() < self.size {
                self.heap.push_front(raw_new_node);
                self.dicc.entry(key_cp).or_insert(Some(new_node));
            } else {
                unsafe{
                    let old_key = (*self.heap.last()).key.to_string();
                    self.heap.remove_last();
                    self.dicc.remove(&old_key);
                }
                self.heap.push_front(raw_new_node);
                self.dicc.entry(key_cp).or_insert(Some(new_node));
            }
        }

    }
    fn getMostRecentKey(&mut self) -> String {
        if self.dicc.len() > 0 {
            unsafe {
                let first =  self.heap.first();
                return (*first).key.to_string();
            };
        }
        return " ".to_string();
    }

    fn getValueFromKey(&mut self, key:String) -> i32{
        let mut result = self.dicc.get_mut(&key);
        if result.is_some() {
            unsafe {
                // println!("{}", type_of(&result));
                let mut node_optional = result.as_mut().unwrap();
                // println!("{}", type_of(&node_optional));
                let mut node = node_optional.as_mut().unwrap();
                let mut raw_node = node.as_mut();
                self.heap.remove(raw_node);
                self.heap.push_front(raw_node);
                return (*raw_node).value
            };
        }
        -1
    }
}


fn main() {
    let mut cache = LRUCache::new(3);
    cache.insert("b".to_string(), 2);
    cache.insert("a".to_string(), 1);
    cache.insert("c".to_string(), 3);

    cache.heap.print();
    println!("{}: ", cache.getMostRecentKey());
    println!("{}: ", cache.getValueFromKey("a".to_string()));
    cache.heap.print();

    cache.insert("d".to_string(), 4);
    cache.heap.print();
    cache.insert("a".to_string(), 5);
    cache.heap.print();
}