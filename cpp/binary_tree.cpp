#include <memory>
#include <vector>
#include <iostream>

struct node {
    int value;
    std::unique_ptr<node> children[2];
    node(int value) 
        : value{value}, children{nullptr, nullptr}
    {

    } 
};

struct binary_tree { 
    std::unique_ptr<node> root;
    binary_tree() : root{nullptr} 
    {}

    std::unique_ptr<node> recursive_insert(node* parent, int value) {
        if (parent == nullptr) {
            return std::make_unique<node>(value);
        } 
        auto idx = (value < parent->value) ? 0 : 1;
        auto curr_child = parent->children[idx].get();  
        auto new_node = recursive_insert(curr_child, value);
        if (curr_child == nullptr) {
            parent->children[idx] = std::move(new_node);
        }
        return nullptr;
    }

    void insert(int value) {
        if (root == nullptr){
            root = std::make_unique<node>(value);
            return;
        }
        recursive_insert(root.get(), value);
    }
    void recursive_print(node* ptr, int level) {
        if(ptr) {
            recursive_print(ptr->children[1].get(), level + 1);
            for (size_t i = 0; i < level; i++){
                std::cout << "    ";
            }
            std::cout << ptr->value << std::endl;
            recursive_print(ptr->children[0].get(), level + 1);
        }
    }

    void print() {
        recursive_print(root.get(), 0);        
    }
};

int main() {
    binary_tree b;
    b.insert(5);
    b.insert(3);
    b.insert(7);
    b.insert(2);
    b.insert(4);
    b.insert(6);
    b.insert(9);
    b.print();
    return 0;
}
