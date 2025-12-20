mod binary_tree;
mod linked_list;
mod lru;
mod sorting;

fn main() {
    println!("=== Sorting Demo ===");
    sorting::demo();

    println!("\n=== Linked List Demo ===");
    linked_list::demo();

    println!("\n=== Binary Tree Demo ===");
    binary_tree::demo();

    println!("\n=== LRU Cache Demo ===");
    lru::demo();
}
