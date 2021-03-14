#include <memory>
#include <vector>
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
    size_t size; 

    linked_list()
        : head{nullptr}, tail{nullptr} ,size{0}
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
        this->size++;
    }

    int remove_head() {
        if (this->head) {
            auto old_value = this->head->value;

            auto new_head = std::move(this->head->next);
            if (new_head == nullptr) {
                this->tail = nullptr;
            }
            this->head = std::move(new_head);
            this->size--;
            return old_value;
        }        
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

template<typename ADT, typename Pred>
void generic_print(ADT ds, Pred pred) {
    for(auto iter = ds.begin(); iter != ds.end(); iter++){
        pred(*iter);
    }
}

int main() {
    auto l = linked_list();
    auto arr = std::vector<int>();
    for (auto i = 0; i < 10; i++) {
        l.push_back(i);
        arr.push_back(i);
    }
    l.print();
    while (l.size > 0) {
        l.remove_head();
        l.print();
    }
    l.print();

    std::cout << "functors >>>\n";
    generic_print(arr, [](auto x) {
        std::cout << x << ", ";
    });
    std::cout << "<<<\n";
    return 0;
}