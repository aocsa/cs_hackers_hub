#include <memory>
#include <iostream>

struct node {
    int value;
    std::unique_ptr<node> next;
    node(int value) : value{value}, next{nullptr}
    {

    } 
};

struct linked_list{
    std::unique_ptr<node> head;
    node* tail;

    linked_list()
        : head{nullptr}, tail{nullptr}
    {
    }

    void push_back(int value) {
        auto new_tail = std::make_unique<node>(value);
        auto raw_tail = new_tail.get();
        if (this->tail != nullptr) {
            tail->next = std::move(new_tail);
        } else {
            this->head = std::move(new_tail);
        }
        this->tail = raw_tail;
    }
    void print() {
        auto node = this->head.get();
        while (node) {
            std::cout << node->value << ", ";
            node = node->next.get();
        }
        std::cout << std::endl;
    }
};

int main() {
    auto l = linked_list();
    l.push_back(0);
    l.push_back(1);
    l.push_back(2);
    l.push_back(3);

    l.print();
    return 0;
}