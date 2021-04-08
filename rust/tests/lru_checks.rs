
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