
#include <unordered_map>
#include <vector>
#include <string>
#include <iostream>
#include <memory>

using namespace std;

struct node{
    string key;
    int value; 
    node* next; 
    node* prev;
    node(string k ="", int v = 0) {
        key = k;
        value = v;
        next = prev = nullptr;
    }
};

struct List{
    std::unique_ptr<node> head;
    std::unique_ptr<node> tail;
    int size;
    List() {
        this->head = std::make_unique<node>();
        this->tail = std::make_unique<node>();
        this->head->next = tail.get();
        this->tail->prev = head.get();
        this->size = 0;
    }

    void push_front(node *new_node){
        insert(new_node, head.get(), head->next);
    }

    void insert(node *new_node, node* prev, node* curr) {
        prev->next = new_node;
        curr->prev = new_node;
        new_node->next =  curr;
        new_node->prev =  prev;
    }

    node* remove_ref(node *ptr) {
        ptr->prev->next = ptr->next;
        ptr->next->prev = ptr->prev;
        return ptr;
    }

    node* remove_last() {
        auto last = this->tail->prev; 
        return remove_ref(last);
    }
    
    string first_key() {
        auto first = this->head->next;
        return first->key;
    }
};

struct LRUCache {
private: 
    // <string, node*>
    unordered_map<string, std::unique_ptr<node>> dicc;
    List list;
    int size;

public:
    LRUCache(int s) {
        this->size = s;
    }
    
    void insert(string key, int value) {
        auto new_node = std::make_unique<node>(key, value);
        if (this->dicc.size() < this->size) {
            // case 1: insert
            this->list.push_front(new_node.get()); // O(1)
            this->dicc[key] = std::move(new_node);
        } else {
            // case 2: remove!
            this->list.push_front(new_node.get()); // O(1)
            this->dicc[key] = std::move(new_node);

            node* old_node = this->list.remove_last(); // O(1)
            this->dicc.erase(old_node->key);
        }
        // assert(this->dicc.size() <= this->size);
    }

    int getValueFromKey(string key) {
        if (this->dicc.find(key) != this->dicc.end()) {
            auto weak_ptr = this->dicc[key].get();
            this->list.remove_ref(weak_ptr); // O(1)
            this->list.push_front(weak_ptr); // O(1)
            return weak_ptr->value;
        }
        return -1;// null, optional<None>
    }
    string getMostRecentKey() {
        if (this->dicc.size() > 0) {
            return this->list.first_key(); // O(1)
        }
        return "";
    }
};

int main() {
	LRUCache lru(3); // instantiate an LRUCache of size 3
	lru.insert("b", 2);
	lru.insert("a", 1);
	lru.insert("c", 3);
	std::cout << lru.getMostRecentKey() << endl; //// "c" was the most recently inserted key
	std::cout << lru.getValueFromKey("a") << endl; //: 1
	
    std::cout << lru.getMostRecentKey() << endl;  // "a" // "a" was the most recently retrieved key
	lru.insert("d", 4); // the cache had 3 entries; the least recently
	std::cout << lru.getValueFromKey("b") << endl; // None // "b" was evicted in the previous operation
	lru.insert("a", 5); // "a" already exists in the cache so its valu
	std::cout << lru.getValueFromKey("a") << endl; //: 5
    return 0;
}