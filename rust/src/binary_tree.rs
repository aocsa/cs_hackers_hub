
struct Node {
    value:i32,
    children: [Option<Box<Node>>; 2]
}

struct BinaryTree{
    root: Option<Box<Node>>
}

fn _recursive_insert(ptr: &mut Option<Box<Node>>, value:i32) -> Option<Box<Node>> {
    if ptr.is_none() {
        return Some(Box::new(Node { value, children: [None, None] }));
    }
    if let Some(parent) = ptr {
        let idx = if value < parent.value { 0 } else { 1 };
        let ret = _recursive_insert(&mut parent.children[idx], value);
        if parent.children[idx].is_none() {
            parent.children[idx] = ret;
        }
    }
    None
}

// doc ref
// https://doc.rust-lang.org/rust-by-example/flow_control/for.html
fn _recursive_print(parent: &Option<Box<Node>>, level:i32){
    if let Some(ptr) = parent {
        _recursive_print(&ptr.children[1], level + 1);
        for _ in 0..level {
            print!("    ");
        }
        println!("{}", ptr.value);
        _recursive_print(&ptr.children[0], level + 1);
    }
}
impl BinaryTree {
    fn new() -> Self {
        BinaryTree{
            root: None
        }
    }
    fn insert(&mut self, value:i32){
        if self.root.is_none() {
            self.root = Some(Box::new(Node { value, children: [None, None] }));
        } else {
            _recursive_insert(&mut self.root, value);
        }
    }
    fn print(&mut self) {
        _recursive_print(&self.root, 0);
    }
}

fn main() {
    let mut b  = BinaryTree::new();
    b.insert(5);
    b.insert(3);
    b.insert(7);
    b.insert(2);
    b.insert(4);
    b.insert(6);
    b.insert(9);
    b.print();
}